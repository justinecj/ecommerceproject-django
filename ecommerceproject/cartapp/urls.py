from django.urls import path
from . import views
app_name = 'cartapp'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('delete/<int:product_id>/', views.full_delete, name='full_delete'),
]