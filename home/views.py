from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):

    peoples = [
        {'name' : 'Vihangraj Madhak', 'age' : 23},
        {'name' : 'Nilay Mokariya', 'age' : 21},
        {'name' : 'Vicky Kaushal', 'age' : 17},
        {'name' : 'Deep Dave', 'age' : 16},
        {'name' : 'Sandeep Maheta', 'age' : 32}
    ]

    vegetable = ['Pumpkin', 'Tomato', 'Potatoe']

    return render(request, "home/index.html", context = {'page': 'Django App', 'peoples' : peoples, 'vegetable': vegetable})

def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a Success page</h1>")