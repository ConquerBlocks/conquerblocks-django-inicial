"""
URL configuration for conquermanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

from .views import home_view, contact_view

urlpatterns = [
    path("", home_view, name="home"),
    path("", include("books.urls", namespace="books")),
    path("contacta-con-nosotros/", contact_view, name="contacto"),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()
