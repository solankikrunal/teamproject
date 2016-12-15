from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Users
import json


def loginpost(request):
	name=request.GET.get("myName");
	password=request.GET.get("myPass");
	print name,password
	request.session["username"]=name
	data=Users(first_name=name,password=password)
	data.save()
	print "done"
	return HttpResponseRedirect("/sulekha/home/")

def home(request):
	name=request.session.get("username");
	return render(request, "home.html",{"uname":name})

def index(request):
	return render(request, "index.html")

def login(request):
	return render(request,"loginPage.html")

def logout(request):
	del request.session['username']
	return HttpResponseRedirect("/sulekha/home/")

def post(request):
	return render(request,"post.html")

