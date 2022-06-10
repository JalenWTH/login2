from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def Home(request):
	try:
		if request.session['signed_in']==True:
			return render(request, 'login2/home.html', {})

	except KeyError:
		return redirect('Login')
		#if signed_in is None, causing a KeyError, redirect to login 


def Login(request):
	if request.method=='POST':
		form=User_Info_Login(request.POST)
		if form.is_valid():
			values=list(form.cleaned_data.items())
			for i in range(len(values)):
				globals()[f'{values[i][0]}']=values[i][1]
				#dynamically creates variables for each field

			for queryset in User_Info.objects.values():
				if queryset['email']==email and queryset['password']==password:
					request.session['signed_in']=True
					request.session.set_expiry(3600)
					return redirect('Home')
					#if user is registered, redirect to home and keep signed in

			registered = False
			return render(request, 'login2/login.html', {'form':form, 'registered':registered})
			# if user is not registered, reload page 

	form=User_Info_Login()
	return render(request, 'login2/login.html', {'form':form})
	#if Get request, render page as normal


def Signup(request):
	if request.method=='POST':
		form=User_Info_Signup(request.POST)
		if form.is_valid():
			values=list(form.cleaned_data.items())
			for i in range(len(values)):
				globals()[f'{values[i][0]}']=values[i][1]
				#dynamically creates variables for each field

			global phone
			while phone.find('-') != -1:
				phone=phone[:phone.find('-')] + phone[phone.find('-')+1:]
				#remove all dashes from phone number if there are any

			for x in User_Info.objects.filter(email__iexact=email).values():
				if len(x) != 0:
					email_already_registered = True
					return render(request, 'login2/signup.html', {'form':form,'email_already_registered':email_already_registered})

			instance=User_Info(fname=fname,lname=lname,phone=phone,email=email,password=password)
			instance.save()
			return redirect('Login')
	else:
		form=User_Info_Signup()
		return render(request, 'login2/signup.html', {'form':form})
		#if GET request, render page as normal