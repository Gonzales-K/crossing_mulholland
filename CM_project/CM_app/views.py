
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all
    context = {'items': items}
    return render(request, 'index.html', context)

def cart(request):
    context = {}
    return render(request, 'index.html', context)

def add_to_cart(request):
    return JsonResponse('working', safe=False)