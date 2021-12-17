from django.shortcuts import render
from django.http import HttpResponse
from . models import product 
from math import ceil
# Create your views here.

def index(request) :
    # products = product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4+ceil((n/4)-(n//4))
    # # params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    # allProds = [[products,range(1,nslides),nslides],
    # [products,range(1,nslides),nslides]]
    allProds = []
    catprods = product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats :
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil(n/4) - (n//4)
        allProds.append([prod,range(1,nSlides),nSlides])
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request) :
    return render(request,'shop/about.html')

def contact(request) :
    return render(request,'shop/contact.html')


def tracker(request) :
    return render(request,'shop/tracker.html')


def search(request) :
    return render(request,'shop/search.html')


def productview(request, myid) :
    # fetch the product using the id 
    product = product.objects.filter(id=myid);
    return render(request,'shop/productview.html',{'product':'product'})

def checkout(request) :
    return render(request,'shop/checkout.html')
