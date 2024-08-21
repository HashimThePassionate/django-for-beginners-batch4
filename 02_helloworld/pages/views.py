from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page_view(request):
    return HttpResponse('<h1><pre>Welcome to Django World</pre></h1>')


def about_page_view(request):
    return HttpResponse('<h1><pre>About Page</pre></h1>')
