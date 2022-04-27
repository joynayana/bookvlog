from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from shop.models import *
from . models import *

# Create your views here.
def cart_details(request,total=0,count=0,ct_items=None):
    try:
        cl_obj=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=cl_obj,active=True)
        for i in ct_items:
            total+=(i.prodt.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'net':total,'count':count,'items': ct_items})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod_obj=product.objects.get(id=product_id)
    try:
        # value = cartlist.objects.filter(user=request.user).values('cart_id').first()
        cartlist_obj=cartlist.objects.get(cart_id=c_id(request),user=request.user)
    except cartlist.DoesNotExist:
        cartlist_obj=cartlist.objects.create(cart_id=c_id(request),user=request.user)
        cartlist_obj.save()
    try:
        items_obj=items.objects.get(prodt=prod_obj,cart= cartlist_obj)
        if items_obj.quan < items_obj.prodt.stock:
            items_obj.quan+=1
        items_obj.save()
    except items.DoesNotExist:
        items_obj=items.objects.create(prodt=prod_obj,cart=cartlist_obj,quan=1)
        items_obj.save()
    return redirect('cartDetails')

def min_cart(request,product_id):
    ct_obj=cartlist.objects.get(cart_id= c_id(request))
    pdt_obj=get_object_or_404(product,id=product_id)
    item_obj=items.objects.get(cart=ct_obj,prodt=pdt_obj)
    if item_obj.quan > 1:
        item_obj.quan-=1
        item_obj.save()
    else:
        item_obj.delete()
    return redirect('cartDetails')

def car_delete(request,product_id):
    ct_obj = cartlist.objects.get(cart_id=c_id(request))
    pdt_obj = get_object_or_404(product, id=product_id)
    item_obj = items.objects.get(cart=ct_obj, prodt=pdt_obj)
    item_obj.delete()
    return redirect('cartDetails')
