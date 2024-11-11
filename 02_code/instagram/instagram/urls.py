"""
URL configuration for instagram project.

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
from django.urls import path

from .views import HomeView, LoginView, RegisterView, ContactView, LegalView, logout_view, ProfileDetailView, ProfileUpdateView, ProfileListView
from django.conf.urls.static import static
from django.conf import settings
from posts.views import PostCreateView, PostDetailView, like_post, like_post_ajax


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/list/', ProfileListView.as_view(), name='profile_list'),
    path('profile/<pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/update/<pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('posts/create/', PostCreateView.as_view(), name="post_create"),
    path('posts/<pk>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/like/<pk>/', like_post, name="post_like"),
    path('posts/like-ajax/<pk>/', like_post_ajax, name="post_like_ajax"),
    path('legal/', LegalView.as_view(), name='legal'),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
