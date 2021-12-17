from django.shortcuts import render
from django.http import HttpResponse
from . models import product,Contact,Checkout
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
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name = name , email = email , phone = phone, desc = desc )
        contact.save()
    return render(request,'shop/contact.html/')


def tracker(request) :
    return render(request,'shop/tracker.html')


def search(request) :
    return render(request,'shop/search.html')


def productview(request, myid) :
    # fetch the product using the id 
    products = product.objects.filter(id=myid);
    print(products)
    return render(request,'shop/productview.html',{'product':products[0]})

def checkout(request,id):
    products = product.objects.filter(id=id)
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address1 = request.POST.get('address1','')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        phone =request.POST.get('phone','')
        checkout = Checkout(name = name , email = email , address = address1, address2 = address2, city = city ,state = state, phone = phone )
        checkout.save()
    
    print(products)
    return render(request,'shop/checkout.html',{'product':products[0]})
    # return render(request,'shop/checkout.html/')

# def shippingAddress(request):
    