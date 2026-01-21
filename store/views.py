from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def product_list(request):
    return Response('samson ok')

@api_view()
def product_detail(response,id):
    return Response(id)