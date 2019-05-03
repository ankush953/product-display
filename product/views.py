from django.shortcuts import render

# import product model from product app
from product.models import Product

# Create your views here.
def homepage(request):
    # retrieve all objects of Product class
    all_product = Product.objects.all()

    showitems = {
        'products':all_product,
        'title':'Homepage'
    }
    return render(request,'homepage.html',context=showitems)
