from django.shortcuts import render
from django.http import HttpResponse
from website.forms import *
# Create your views here.

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'index.html', {'form': MessageForm(),'registrationform': RegistrationForm()})

def animepage(request):
	context={

	}
	return render(request,"animepage.html",{'form': MessageForm(),'registrationform': RegistrationForm()})

def mangapage(request):
	context={

	}
	return render(request,"mangapage.html",{'form': MessageForm(),'registrationform': RegistrationForm()})

def communitypage(request):
	context={

	}
	return render(request, "communitypage.html", {'form': MessageForm(),'registrationform': RegistrationForm()})

def industrypage(request):
	context={

	}
	return render(request, "industrypage.html", {'form': MessageForm(),'registrationform': RegistrationForm()})

def watchpage(request):
	context={

	}
	return render(request, "watchpage.html", {'form': MessageForm(),'registrationform': RegistrationForm()})

def helppage(request):
	context={

	}
	return render(request, "helppage.html", {'form': MessageForm(),'registrationform': RegistrationForm()})

