from django.shortcuts import render
from django.http import HttpResponse
from core.erp.models import Category

# Create your views here.

def myFirstView(request):
    return render(request, 'body.html')