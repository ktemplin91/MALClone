from django.shortcuts import render
from django.http import HttpResponse
from website.forms import *
# Create your views here.

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'index.html', {'form': MessageForm()})

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

