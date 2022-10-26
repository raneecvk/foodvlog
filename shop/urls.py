from . import views
from django.urls import path,include


urlpatterns = [
   path('',views.home,name='home'),
   path('<slug:c_slug>/',views.home,name='prod_cat'),
   path('<slug:c_slug>/<slug:product_slug>',views.prodtdetails,name='details'),
   path('search',views.searching,name='search')
]