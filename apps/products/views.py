from django.shortcuts import render, redirect
from .models import Product
# Create your views here.

def index(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'products/index.html',context)

def new(request):

    return render(request, 'products/new.html')

def create(request):

    price = request.POST['price']
    print float(price)
    Product.objects.create(name = request.POST['name'], description = request.POST['description'], price = float(request.POST['price']))

    return redirect('/products/new')

def show(request, id):
    context = {
        'product' : Product.objects.get(id = id)
    }
    return render(request, 'products/show.html', context)


def edit(request, id):
    context = {
        'id' : id
    }

    return render(request,'products/edit.html', context)

def destroy(request, id):
    Product.objects.get(id = id).delete()
    return redirect('/products')

def update(request, id):
    product = Product.objects.get(id = id)

    if request.POST['name']:
        product.name = request.POST['name']
    if request.POST['description']:
        product.description = request.POST['description']
    if request.POST['price']:
        product.price = float(request.POST['price'])

    product.save()

    return redirect('/products')