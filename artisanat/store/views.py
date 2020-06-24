from django.shortcuts import render

from .models import Artisanat


def index(request):
    artisanats = Artisanat.all()
    context = {
        "artisanats":artisanats
    }
    return render(request, 'store/index.html', context)
    
def category(request, id):
    category = Artisanat.find(id)
    artisanats = Artisanat.all()  
    context = {
        "artisanats":artisanats,
        "category":category
    }
    return render(request, 'store/category.html', context)
    