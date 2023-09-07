from django.shortcuts import render

from records.models import Product


# Create your views here.
def home(request):
    return render(request, "home.html")


def products_list(request):
    products = Product.objects.all()
    return render(request, "records/products.html", {"products": products})

