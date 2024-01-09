from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("info", views.info, name="info"),
    path("login_view", views.login_view, name="login_view"),
    path("registerd", views.registerd, name="registerd")
]