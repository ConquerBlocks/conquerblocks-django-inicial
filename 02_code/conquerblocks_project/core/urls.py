from django.urls import path

from .views import home, about_us, register, login, contact

app_name = "core"

urlpatterns = [
  path("", home, name="home"),
  path("sobre-nosotros/", about_us, name="about_us"),
  path("registro/", register, name="register"),
  path("login/", login, name="login"),
  path("contacta-con-nosotros/", contact, name="contact"),
]
