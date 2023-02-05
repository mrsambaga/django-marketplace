from django.shortcuts import render, redirect
from item.models import *
from .forms import *

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all()
    return render(request, 'marketplace_app/index.html', {'items' : items, 'categories' : category})

def contact(request):
    return render(request, 'marketplace_app/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm

    return render(request, 'marketplace_app/signup.html', {'form' : form})