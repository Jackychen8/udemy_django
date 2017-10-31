# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User

# Create your views here.

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records':webpages_list}
	#my_dict = {'insert_me': "Hello I am from views.py!"}
	return render(request, 'first_app/index.html', context=date_dict)
	#return HttpResponse("Hello World!")

def users(request):
	users_list = User.objects.order_by('email')
	user_dict = {'user_records':users_list}

	# -> this file -> templates/first_app/users.html
	return render(request, 'first_app/users.html', context=user_dict)