from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('reset-password/', views.ResetPassword.as_view(), name='reset-password'),
    path('set-newpassword/', views.SetNewPass.as_view(), name='set-newpassword'),
 # Add a comma here
    # Other URL patterns for authentication
]
