import collections
from re import X
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.
def say_hello(request):
    #keyword=value
    queryset = Product.objects.filter(description__isnull=True)
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Product.objects.filter(title__startswith='coffee')
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(collection__id__range=(1,2,3))
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    # queryset = Product.objects.filter(unit_price__gt=20)
    # for product in query_set:
    #     print(product)
    # list(query_set)
    # query_set[0:5]
    # query_set.filter().filter().order_by()

    return render(request, 'hello.html', {'name':'Osama','products': list(queryset)})