from django.urls import path
from .views import landing, CustomLoginView
from django.contrib.auth.views import LogoutView
from .views import pallet_admin_view, dashboard_view, log_view

urlpatterns = [
    path('', landing, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('pallets/admin/', pallet_admin_view, name='pallet_admin'),
    path('pallets/dashboard/', dashboard_view, name='dashboard'),
    path('logs/', log_view, name='log_view'),
]