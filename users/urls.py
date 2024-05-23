from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .forms import LoginForm, ChangePasswordForm, ResetPasswordForm, ConfirmPasswordForm
from .views import SignUp, UpdateProfileInfoView


app_name = "users"

urlpatterns = [
    # Login and logout views.
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
            form_class=LoginForm,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    # Registration and update profile-info views.
    path("signup/", SignUp.as_view(), name="signup"),
    path("profile/", UpdateProfileInfoView.as_view(), name="profile"),
    # Password change views.
    path(
        "password_change/",
        PasswordChangeView.as_view(
            template_name="users/password_change_form.html",
            success_url=reverse_lazy("users:password_change_done"),
            form_class=ChangePasswordForm,
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
        name="password_change_done",
    ),
    # Password reset views.
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            success_url=reverse_lazy("users:password_reset_done"),
            email_template_name="users/password_reset_email.html",
            form_class=ResetPasswordForm,
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            form_class=ConfirmPasswordForm,
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
