# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
	return render(request,'basic_form/index.html')

def form_help_view(request):
	form = forms.HelpForm()

	if request.method == 'POST':
		form = forms.HelpForm(request.POST)

		if form.is_valid():
			#.save()
			print("SAVED DATA")

	return render(request,'basic_form/help_form_page.html',{'form':form})


def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			# basic, default true probably
			print("VALIDATION SUCCESS!")
			print("NAME: " + form.cleaned_data['name'])
			print("EMAIL: " + form.cleaned_data['email'])
			print("TEXT: " + form.cleaned_data['text'])
			#.save()

	return render(request,'basic_form/form_page.html',{'form':form})