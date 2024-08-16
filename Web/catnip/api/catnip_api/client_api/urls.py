from django.urls import path

from . import routers

urlpatterns = [
    path("token-check", routers.token_check, name="token-check"),
    path("login", routers.login, name="login"),
    path("forgot-password", routers.forgot_password, name="forgot-password"),
    path("logout", routers.logout, name="logout"),
    path("generate-report", routers.request_cat, name="generate-report"),
]