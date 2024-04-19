from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,"index.html")

def success_page(request):
    return HttpResponse("<h1>this is a sucess page </h1>")