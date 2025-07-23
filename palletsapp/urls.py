from django.urls import path
from .views import landing, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', landing, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]