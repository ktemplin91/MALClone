from django.shortcuts import render
from django.http import HttpResponse
from website.forms import *
import json
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


def profilepage(request):
	context={

	}
	return render(request, "userprofile.html", {'form': MessageForm(),'registrationform': RegistrationForm()})	


def login(request):                                                                                                                         
    if request.method == 'POST':                                                                                                                                                                                                           
        login_form = AuthenticationForm(request, request.POST)
        response_data = {}                                                                              
        if login_form.is_valid():                                                                                                           
            response_data['result'] = 'Success!'
            response_data['message'] = 'You"re logged in' 
        else:
            response_data['result'] = 'failed'
            response_data['message'] = 'You messed up'   

        return HttpResponse(json.dumps(response_data), content_type="application/json") 