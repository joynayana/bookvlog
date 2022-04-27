from django.urls import path,include
from shop import views as s

urlpatterns=[
    path('',s.home,name='home'),
    path('<slug:c_slug>/',s.home,name="prod_cat"),
    path('<slug:c_slug>/<slug:product_slug>',s.prodDetails,name='details'),
    path('search',s.searching,name='search'),

]