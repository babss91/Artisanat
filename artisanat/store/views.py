from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'store/index.html', context)
    
