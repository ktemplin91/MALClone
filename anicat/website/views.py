from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from website.forms import *
import json
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'index.html', {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Home'})

def animepage(request):
	context={

	}
	return render(request,"animepage.html",{'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Anime'})

def mangapage(request):
	context={

	}
	return render(request,"mangapage.html",{'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Manga'})

def communitypage(request):
	context={

	}
	return render(request, "communitypage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Community'})

def industrypage(request):
	context={

	}
	return render(request, "industrypage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Industry'})

def watchpage(request):
	context={

	}
	return render(request, "watchpage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Watch'})

def helppage(request):
	context={

	}
	return render(request, "helppage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Help'})

@login_required(login_url='/', redirect_field_name=None)
def profilepage(request,username):
    u = User.objects.get(username=username)
    return render(request, "userprofile.html", {'form': MessageForm(),'registrationform': RegistrationForm()})


@csrf_protect
def login_view(request):
    dic = {}
    if request.method == 'POST':
        login_form = MessageForm(request.POST or None)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print(login_form['password'])
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponse(json.dumps({"success" : True}), content_type="application/json")
            else:
                print("Here1")
                return HttpResponse(json.dumps({"success" : False}), content_type="application/json")
        else:
            print("Here2")
            return HttpResponse(json.dumps({"success" : False}), content_type="application/json")
    return HttpResponse(json.dumps({"success" : False}), content_type="application/json")

@csrf_protect
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def validate_username(request):
    username = request.GET.get('username', None)
    data = { 'is_taken' : User.objects.filter(username__iexact=username).exists()}
    return HttpResponse(json.dumps(data), content_type="application/json")

def validate_email(request):
    email = request.GET.get('email', None)
    data = { 'is_taken' : User.objects.filter(email__iexact=email).exists()}
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_protect
def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password'],
            )
        else:
            print(request)
    return HttpResponse(json.dumps({'success' : 'success'}), content_type="application/json")
