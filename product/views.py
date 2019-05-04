from django.shortcuts import render

# import product model from product app
from product.models import Product, Review

# to perform queries
from django.db.models import Q

# Create your views here.


def homepage(request):
    # if user queried something
    query = request.GET.get('query', None)
    if query:
        products = Product.objects.filter(Q(name__icontains=query) |
                                          Q(brand__brandName__icontains=query)
                                          ).distinct()
    else:
        # retrieve all objects of Product class
        products = Product.objects.all()

    showitems = {
        'products': products,
        'title': 'Homepage'
    }
    return render(request, 'homepage.html', context=showitems)


def detail(request,id):
    product = Product.objects.filter(id=id).first()
    reviews = Review.objects.filter(product__id=id)
    details = {
        'product':product,
        'reviews':reviews,
        'title':product.name,
    }
    return render(request,'details.html',context=details)
