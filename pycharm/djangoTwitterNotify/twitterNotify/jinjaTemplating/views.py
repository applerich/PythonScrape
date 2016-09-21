from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'jinjaTemplating/home.html')

def contact(request):
    return render(request, 'jinjaTemplating/basic.html', {'content': ['contact me at: ', 'zhibolau@gmail.com']})