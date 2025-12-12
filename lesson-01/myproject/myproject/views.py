from django.http import HttpResponse;

def homepage(request):
    return HttpResponse("Hello world! From Home page.");

def aboutpage(request):
    return HttpResponse("Hello, I'm about page");