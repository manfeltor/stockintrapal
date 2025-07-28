from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from .models import PalletStock, PalletLog
from django.forms.models import model_to_dict
from django.utils.timezone import now
from .forms import StockInForm, StockOutForm, ResetStockForm
from django.db.models import Sum

# Create your views here.

LOG_ACTION_STOCK_IN = 'stock_in'
LOG_ACTION_STOCK_OUT = 'stock_out'
LOG_ACTION_RESET = 'reset'

def log_current_stock(user, action_label):
    
    snapshot = []

    for obj in PalletStock.objects.all():
        snapshot.append(model_to_dict(obj))

    PalletLog.objects.create(
        username=user.username,
        action=action_label,
        payload={
            'snapshot': snapshot,
            'timestamp': now().isoformat(),
        }
    )

def landing(request):
    form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})

class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def form_invalid(self, form):
        return redirect(f"{reverse_lazy('home')}?error=1")
    
@login_required
def pallet_admin_view(request):
    in_form = StockInForm()
    out_form = StockOutForm()
    reset_form = ResetStockForm()

    if request.method == 'POST':
        if 'stock_in_submit' in request.POST:
            in_form = StockInForm(request.POST)
            if in_form.is_valid():
                quality = in_form.cleaned_data['quality'] or None
                quantity = in_form.cleaned_data['quantity']

                obj, _ = PalletStock.objects.get_or_create(
                    quality=quality,
                    status='ok',
                    defaults={'quantity': 0}
                )
                obj.quantity += quantity
                obj.save()
                log_current_stock(request.user, LOG_ACTION_STOCK_IN)
                return redirect('pallet_admin')

        elif 'stock_out_submit' in request.POST:
            out_form = StockOutForm(request.POST)
            if out_form.is_valid():
                quality = out_form.cleaned_data['quality'] or None
                quantity = out_form.cleaned_data['quantity']

                try:
                    obj = PalletStock.objects.get(quality=quality, status='ok')
                    if obj.quantity < quantity:
                        return redirect('/?error=1')
                    obj.quantity -= quantity
                    obj.save()
                    log_current_stock(request.user, LOG_ACTION_STOCK_OUT)
                    return redirect('pallet_admin')
                except PalletStock.DoesNotExist:
                    return redirect('/?error=2')

        elif 'reset_submit' in request.POST:
            reset_form = ResetStockForm(request.POST)
            if reset_form.is_valid():
                quality = reset_form.cleaned_data['quality'] or None
                quantity = reset_form.cleaned_data['quantity']

                obj, _ = PalletStock.objects.get_or_create(
                    quality=quality,
                    status='ok',
                    defaults={'quantity': 0}
                )
                obj.quantity = quantity
                obj.save()
                log_current_stock(request.user, LOG_ACTION_RESET)
                return redirect(f'/?reset=1&quality={quality or "sin calidad"}&qty={quantity}')

    return render(request, 'pallet_admin.html', {
        'in_form': in_form,
        'out_form': out_form,
        'reset_form': reset_form,
    })

@login_required
def dashboard_view(request):
    def get_stock(quality, status):
        return PalletStock.objects.filter(quality=quality, status=status).aggregate(
            total=Sum('quantity')
        )['total'] or 0

    total_all = PalletStock.objects.aggregate(total=Sum('quantity'))['total'] or 0
    total_ok = PalletStock.objects.filter(status='ok').aggregate(total=Sum('quantity'))['total'] or 0

    context = {
        'a_ok': get_stock('A', 'ok'),
        'a_scrap': get_stock('A', 'scrap'),
        'b_ok': get_stock('B', 'ok'),
        'b_scrap': get_stock('B', 'scrap'),
        'null_ok': get_stock(None, 'ok'),
        'null_scrap': get_stock(None, 'scrap'),

        'total_stock': total_all,
        'total_ok_stock': total_ok,
    }

    return render(request, 'dashboard.html', context)

@login_required
def log_view(request):
    logs = PalletLog.objects.order_by('-timestamp')[:100]  # limit for performance
    return render(request, 'logs.html', {'logs': logs})