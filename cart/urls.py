from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('cartdetails',views.cart_details,name='cartdetails'),
    path('add/<int:product_id>/',views.addcart,name='addcart'),
    path('cart_min/<int:product_id>/',views.min_cart,name='cart_min'),
    path('delete/<int:product_id>/',views.cart_delete,name='delete')
]