from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or email address",
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control", "name": "username"}),
    )
    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.PasswordInput(attrs={"class": "form-control", "name": "password"}),
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control", "name": "username"}),
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"class": "form-control", "name": "email"}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "name": "password1"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "name": "password2"}
        ),
    )

    image = forms.ImageField(
        label="Profile image",
        widget=forms.FileInput(attrs={"class": "form-control", "name": "image"}),
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2", "image")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(
                "A user is already registered with this email address."
            )
        return email


class UpdateProfileInfoForm(forms.ModelForm):
    image = forms.ImageField(
        label="Profile image",
        widget=forms.FileInput(attrs={"class": "form-control", "name": "image"}),
        required=False,
    )

    username = forms.CharField(
        disabled=True,
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control", "name": "username"}),
    )
    email = forms.EmailField(
        disabled=True,
        label="Email address",
        widget=forms.EmailInput(attrs={"class": "form-control", "name": "email"}),
    )

    class Meta:
        model = get_user_model()
        fields = ("image", "username", "email", "first_name", "last_name")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "name": "first_name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "name": "last_name"}
            ),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "name": "old_password"}
        ),
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "name": "new_password1"}
        ),
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "name": "new_password2"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ("old_password", "new_password1", "new_password2")


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"class": "form-control", "name": "email"}),
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)


class ConfirmPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "name": "new_password1"}
        ),
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "name": "new_password2"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ("new_password1", "new_password2")
