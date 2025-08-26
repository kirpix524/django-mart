from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone")

class UserUpdateForm(UserChangeForm):
    password = None  # прячем пароль в обычной форме профиля
    class Meta:
        model = User
        fields = ("email", "phone", "date_of_birth")