from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   #template = loader.get_template('website/base.html')
   # return HttpResponse("Hello, world. You're at the polls index.")
   context ={

   }
   return render(request, "index.html",{})

def animepage(request):
	context={

	}
	return render(request,"animepage.html",{})

def mangapage(request):
	context={

	}
	return render(request,"mangapage.html",{})

def communitypage(request):
	context={

	}
	return render(request, "communitypage.html", {})

def industrypage(request):
	context={

	}
	return render(request, "industrypage.html", {})

def watchpage(request):
	context={

	}
	return render(request, "watchpage.html", {})

def helppage(request):
	context={

	}
	return render(request, "helppage.html", {})