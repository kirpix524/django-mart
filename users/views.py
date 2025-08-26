from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from .forms import UserCreateForm

User = get_user_model()

class SignUpView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class ProfileView(TemplateView):
    template_name = "profile.html"