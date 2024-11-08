'''
    this file is responsible for the urls of the user_profiles app
'''
from django.urls import path
from user_profiles.views import (
    CreateView, LoginView, LogoutView,
    UpdateProfileView, UserAccountView, UserAccountLogoutView,
    UserAccountProfileView, ChangePasswordView, ResetPasswordView,
    ResetCodeView, ResetChangePasswordView, ResendResetCodeView,
    VerificationCodeView
)

app_name = 'user_profiles'


urlpatterns = [
    path('register/', CreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/update/', UpdateProfileView.as_view(),
         name='update_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verification-code/', VerificationCodeView.as_view(),
         name='user_verification_code'),
    #     path('email-confirmation/<str:token>/', EmailConfirmation.as_view(),
    #     name = 'email_confirmation'),
    path('user-account/', UserAccountView.as_view(), name='user_account'),
    path('user-account-logout/', UserAccountLogoutView.as_view(),
         name='user_logout'),
    path('user-account-profile/', UserAccountProfileView.as_view(),
         name='user_account_profile'),
    path('user-change-password/', ChangePasswordView.as_view(),
         name='user_change_password'),
    path('user-reset-password/', ResetPasswordView.as_view(),
         name='user_reset_password'),
    path('user-reset-code/', ResetCodeView.as_view(),
         name='user_reset_code'),
    path('user-reset-change-password/',
         ResetChangePasswordView.as_view(), name='user_reset_change_password'),
    path('user-resend-reset-code/', ResendResetCodeView.as_view(),
         name='user_resend_reset_code'),
]
