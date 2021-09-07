"""LaProfumeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Base, name='Base'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='Accedi'),
    path('register/', views.register, name='Registration'),
    path('logout/', views.logout_view, name='Logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('search_bar/', views.SearchBar, name='SearchBar'),
    path('search_bar/<int:pk>/products_list/', ProductList.as_view(), name='ProductList'),
    path('review_added/<int:id>', views.product_review, name='ProductReview'),
    path('brand/', BrandList.as_view(), name='brand-list'),
    path('price/', views.price, name='price'),
    path('ajax_filter_price/', views.filter_price, name='filter-price'),
    path('men_perfumes/', MenPerfumes.as_view(), name='men-perfumes'),
    path('women_perfumes/', WomenPerfumes.as_view(), name='women-perfumes'),
    path('recommended_products/', views.recommended_products_view, name='recommended-products'),
    path('', include('carts.urls')),
]

# to support and show media & static files in developer mode
if settings.DEVEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)