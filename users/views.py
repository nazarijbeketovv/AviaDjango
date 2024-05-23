from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, UpdateProfileInfoForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")
    template_name = "users/signup.html"


class UpdateProfileInfoView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UpdateProfileInfoForm
    success_url = reverse_lazy("users:profile")
    template_name = "users/profile.html"
    extra_context = {"default_image": settings.DEFAULT_PROFILE_IMAGE}

    def get_object(self):
        return self.request.user
