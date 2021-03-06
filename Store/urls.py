from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Store'

urlpatterns = [

    path('', views.base, name='Base'),
    path('login/', views.login_view, name='Accedi'),
    path('register/', views.register, name='Registration'),
    path('logout/', views.logout_view, name='Logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('search_bar/', views.search_bar, name='SearchBar'),
    path('search_bar/<int:pk>/products_list/', ProductList.as_view(), name='ProductList'),
    path('review_added/<int:id>', views.product_review, name='ProductReview'),
    path('price/', views.price, name='price'),
    path('ajax_filter_price/', views.filter_price, name='filter-price'),
    path('men_perfumes/', MenPerfumes.as_view(), name='men-perfumes'),
    path('women_perfumes/', WomenPerfumes.as_view(), name='women-perfumes'),
    path('recommended_products/', views.recommended_products_view, name='recommended-products'),
    path('lista_prodotti/', views.lista_prodotti_amministratore, name='lista-prodotti'),
    path('modifica_prodotto/<int:pk>/', views.modifica_prodotto, name='modifica-prodotto'),
    path('send_mail/<int:id>/', views.send_email, name='send-email'),
]

# per mostrare file multimediali e statici
if settings.DEVEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
