from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   #template = loader.get_template('website/base.html')
   # return HttpResponse("Hello, world. You're at the polls index.")
   context ={

   }
   return render(request, "index.html",{})
