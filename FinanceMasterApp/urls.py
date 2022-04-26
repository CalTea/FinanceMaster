from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import (AssetCreateView, AssetUpdateView, AssetDeleteView, AssetDetailView)

urlpatterns = [
    path('', views.index, name = 'index'),
    path('addasset/', AssetCreateView.as_view(), name='addasset'),
    path('asset/<int:pk>/', AssetDetailView.as_view(), name='asset'),
    path('asset/<int:pk>/update/', AssetUpdateView.as_view(), name='updateasset'),
    path('asset/<int:pk>/delete/', AssetDeleteView.as_view(), name='deleteasset'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('cryptodata/', views.cryptodata, name ='cryptodata'),
]