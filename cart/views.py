
from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_details(request,tot=0,count=0,ct_items=None):
    try:
        ct1=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct1,active=True)
        for i in ct_items:
            tot+=(i.prodt.price*i.quandity)
            count+=i.quandity
        

    except ObjectDoesNotExist:
        pass
    
    return render(request,'cart.html',{'t':tot,'ci':ct_items,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
   
    return ct_id

def addcart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct1=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct1=cartlist.objects.create(cart_id=c_id(request))
        ct1.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct1)
        if c_items.quandity < c_items.prodt.stock:
            c_items.quandity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quandity=1,cart=ct1)
        c_items.save()

    return redirect("cartdetails")

def min_cart(request,product_id):
    ct1=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct1)
    if c_items.quandity > 1:
        c_items.quandity-=1
        c_items.save()
    else:
        c_items.delete()

    return redirect('cartdetails')

def cart_delete(request,product_id):
    ct1=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct1)
    c_items.delete()
    return redirect('cartdetails')


