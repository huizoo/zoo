from django.shortcuts import render

# Create your views here.

def index(request):
    name = 'KEVIN'
    age = 21
    colors = ['red', 'black', 'white']
    context = {
        'name': name,
        'age': age,
        'colors': colors,
    }
    return render(request, 'myapp/index.html', context)