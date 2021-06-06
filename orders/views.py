from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from music_store.models import *
from .utils import cookieCart, cartData, guestOrder


def cart(request):

    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

            
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'orders/cart.html', context)


def checkout(request):

    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'orders/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    albumId = data['albumId']
    action = data['action']

    print('Action:', action)
    print('AlbumId:', albumId)

    customer = request.user.customer
    album = Album.objects.get(id=albumId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, album=album)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def proccessOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer = customer,
        order = order,
        address = data['shipping']['address'],
        city = data['shipping']['city'],
        state = data['shipping']['state'],
        zipcode = data['shipping']['zipcode'],
    )

    print('Data:', request.body)
    return JsonResponse('Payment completed', safe=False)