from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def landing(request):
    form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'base.html'  # We're using the modal in base.html
    redirect_authenticated_user = True

    def form_invalid(self, form):
        return redirect(f"{reverse_lazy('home')}?error=1")
