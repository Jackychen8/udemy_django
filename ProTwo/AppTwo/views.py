# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
	my_dict = {'insert_help': "Hello I am here to help!"}
	return render(request, 'help.html', context=my_dict)
