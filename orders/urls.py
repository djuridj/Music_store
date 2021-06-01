from django.urls import path
from orders import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('proccess_order/', views.proccessOrder, name="proccess_order"),
]