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
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' }
    return render(request, 'index.html', {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Home', 'dic' : dic})

def animepage(request):
    context={

    }
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' }
    return render(request,"animepage.html",{'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Anime', 'dic' : dic})

def mangapage(request):
    context={

    }
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' }
    return render(request,"mangapage.html",{'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Manga', 'dic' : dic})

def communitypage(request):
    context={

    }
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' }
    return render(request, "communitypage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Community', 'dic' : dic})

def industrypage(request):
    context={

    }
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' }
    return render(request, "industrypage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Industry', 'dic' : dic})

def watchpage(request):
    context={

    }
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' }
    return render(request, "watchpage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Watch', 'dic' : dic})

def helppage(request):
    context={

    }
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' }
    return render(request, "helppage.html", {'form': MessageForm(),'registrationform': RegistrationForm(), 'current_path' : 'Help', 'dic' : dic})

@login_required(login_url='/', redirect_field_name=None)
def profilepage(request,username):
    #if request.user.is_authenticated():
     #   return HttpResponseRedirect(reverse('profilepage', kwargs={'username': request.user.username}))   
    dic = { 'Home' : '/', 'Anime' : 'anime', 'Manga' : 'manga', 'Community' : 'community', 'Industry' : 'industry' , 'Watch' : 'watch', 'Help' : 'help' , 'Profile' : 'profile' }
    u = User.objects.get(username=username)
    return render(request, "userprofile.html", {'form': MessageForm(),'registrationform': RegistrationForm(),'current_path' : 'Profile' ,'dic' : dic})


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
