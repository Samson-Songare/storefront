from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product,Collection,Order,OrderItem
from django.db import connection
# from tags.models import 
from django.db import transaction



# Create your views here.


def say_hello(request):
    # with connection.cursor() as cursor:
    #     cursor.execute()
    return render(request, "hello.html", {'name': 'samson','result':''})
