from django.urls import path
from .views import RegisterView, LoginView, LogoutView, activate_user_view
from .VerifyEmail import VerifyEmailView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('activate-user/', activate_user_view, name='activate-user'),

]
