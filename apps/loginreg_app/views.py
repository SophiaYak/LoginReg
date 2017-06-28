from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	context ={ 'members': User.objects.all()}
	return render(request, "loginreg_app/index.html",context)

def registration(request):
	context ={ 'user_first': request.POST['first_name'],
	'user_last': request.POST['last_name'], 'user_email': request.POST['email'],
	'user_pass': request.POST['pass'], 'user_confpass': request.POST['confpass']}
	result = User.objects.checks(context)
	request.session
	if result['succeed']:
		messages.success(request, "Success! Welcome, {}!".format(context['user_first']))
		request.session['email']=context['user_email']
		return redirect('/success')
	else:
		for error in result['data']:
			messages.error(request, error)
		return redirect('/')

def success(request):
	current = User.objects.filter(email=request.session['email'])
	if current:
		return render(request,"loginreg_app/success.html")
	else:
		return redirect('/')