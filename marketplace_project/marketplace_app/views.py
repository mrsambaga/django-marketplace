from django.shortcuts import render
from item.models import *

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all()
    return render(request, 'marketplace_app/index.html', {'items' : items, 'category' : category})

def contact(request):
    return render(request, 'marketplace_app/contact.html')
