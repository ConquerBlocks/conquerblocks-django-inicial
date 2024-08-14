from django.urls import path

from .views import home, about_us, register, login_view, contact, logout_view

app_name = "core"

urlpatterns = [
  path("", home, name="home"),
  path("sobre-nosotros/", about_us, name="about_us"),
  path("registro/", register, name="register"),
  path("login/", login_view, name="login"),
  path("logout/", logout_view, name="logout"),
  path("contacta-con-nosotros/", contact, name="contact"),
]
