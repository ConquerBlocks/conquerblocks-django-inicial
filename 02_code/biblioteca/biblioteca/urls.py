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
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings

from .views import home_view, contact_view, search_view

from django.conf.urls.i18n import i18n_patterns
from django.conf import settings


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Incluir la vista 'set_language'
] + debug_toolbar_urls()

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("buscar/", search_view, name="search"),
    path("", home_view, name="home"),
    path('editorial/', include('books.urls.editorial_url', namespace='editorial')),
    path('autor/', include('books.urls.autor_url', namespace='autor')),
    path('libro/', include('books.urls.libro_url', namespace='libro')),

    path("contacta-con-nosotros/", contact_view, name="contacto"),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]
