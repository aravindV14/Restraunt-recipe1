from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):

    peoples =[
        {"name":"aravind","age":21},
        {"name":"abhiram","age":16},
        {"name":"shiva","age":22},
        {"name":"varun",'age':23},
        {"name":"sharath","age":25},
    ]
    vegetables =["pumpkin",'tomato',"potato"]
    return render(request, 'home/index.html',context={"peoples":peoples,"vegetables":vegetables,"page":"django"}) 

def success_page(request):
    return HttpResponse("<h1>this is a sucess page </h1>")

def about(request):

    return render(request ,'home/about.html',context={"page":'about'})

def contact(request):
    return render(request ,'home/contact.html',context={"page":'contact'})
