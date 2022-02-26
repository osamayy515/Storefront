from re import X
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# Create your views here.
def say_hello(request):
    query_set = Product.objects.all()

    for product in query_set:
        print(product)

    # list(query_set)
    # query_set[0:5]
    # query_set.filter().filter().order_by()

    return render(request, 'hello.html', {'name':'Osama'})