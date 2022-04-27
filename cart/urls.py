from django.urls import path
from . import views
urlpatterns = [
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('addtocart/<int:product_id>',views.add_cart,name='addcart'),
    path('dec/<int:product_id>', views.min_cart, name='decrement'),
    path('remove/<int:product_id>', views.car_delete, name='remove'),

]
