from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileView

urlpatterns = [
    # регистрация
    path("signup/", SignUpView.as_view(), name="signup"),

    # логин/логаут (можно оставить дефолтные вьюхи Django)
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # страница профиля
    path("profile/", ProfileView.as_view(), name="profile"),

    # (опционально) смена/сброс пароля
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]