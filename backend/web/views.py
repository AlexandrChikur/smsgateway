from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm
from .forms import SignupUserForm


class MainPageView(TemplateView):
    template_name = "web/index.html"


class LoginUserView(LoginView):
    template_name = "web/login.html"
    form_class = LoginUserForm
    success_url = reverse_lazy("url_mainpage")


class SignupUserView(CreateView):
    model = User
    template_name = "web/signup.html"
    form_class = SignupUserForm
    success_url = reverse_lazy("url_mainpage")

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)

        return form_valid


class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("url_mainpage")
