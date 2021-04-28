from django.shortcuts import render
from .models import Products
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    my_context = {
        'form':form
    }
    return render(request, "products/product_create.html",my_context)

def product_detail_view(request):
    obj = Products.objects.get( id = 1)
    my_context = {
        "object": obj
    }
    return render(request, "products/product_detail.html",my_context)

""" #def search_view(request):
    print(request.GET.get('title'))
    print(request.POST)
    context = {
    }
    return render(request, "search.html", context) """

def search_view(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Products.objects.create(**form.cleaned_data)
        else :
            print(form.errors)
    context = {
        'form' : form
    }
    return render(request, "search.html", context)