# from django.http import HttpResponse;
from django.shortcuts import render;

def homepage(request):
    # return HttpResponse("Hello world! From Home page.");
    return render(request, 'home.html');

def aboutpage(request):
    # return HttpResponse("Hello, I'm about page");
    return render(request, 'about.html')