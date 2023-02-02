from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'marketplace_app/index.html')
