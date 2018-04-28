from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django import forms
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse
from django.template import RequestContext
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegisterForm, LoginForm
from .models import Category, Product
from cart.forms import CartAddProductForm


MIN_PASSWORD_LENGTH = 6



#@csrf_protect
def index(request):
    return render(request,'index.html')



#@csrf_protect
def register(request):
	if request.method =='POST':
		rf = RegisterForm(request.POST)
		if rf.is_valid():
			cd = rf.cleaned_data
			if User.objects.filter(username = cd['username']).exists():
				print('username already exists!')
				error_msg = "username already exists. Please pick another one."
				return render_to_response('register.html', {'rf': rf, 'error_msg': error_msg})
			if len(cd['password']) < MIN_PASSWORD_LENGTH:
				print('Password is too short!')
				error_msg = "Password is too short! Please enter a password longer than 6 chars."
				return render_to_response('register.html', {'rf': rf, 'error_msg': error_msg})
			rf.save()
			user = authenticate(username = cd['username'],password = cd['password'])
			auth_login(request,user)
			return redirect('shop:login')
	else:
		rf = RegisterForm()
	return render(request,"register.html",{'rf':rf})


#@csrf_exempt
#@csrf_protect
def login(request):
	if request.method == 'POST':
		lf = LoginForm(request.POST)
		if lf.is_valid():
			cd = lf.cleaned_data
			user = authenticate(request,username = cd['username'],password = cd['password'])
			if user is not None:
				auth_login(request,user)
				return render(request, 'product_list.html', {'category_slug':None})
#return render_to_response("product_list.html", category_slug=None)
			else:
				error_msg = "Please enter the correct username and password."
				return render_to_response('login.html',{'lf':lf,'error_msg': error_msg})
	else:
		lf = LoginForm()
	return render_to_response('login.html',{'lf':lf})
'''
@csrf_protect
def login(request):
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            cd = lf.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None:
                auth_login(request,user)
				return redirect('shop:product_list')
#return render(request, 'product_list.html', context=RequestContext(request))
            else:
                error_msg = "Please enter the correct username and password."
                return render_to_response('login.html',{'lf':lf,'error_msg': error_msg})
    else:
        lf = LoginForm()
    return render_to_response('login.html',{'lf':lf})
'''


#@csrf_protect
@login_required
def logoutView(request):
    logout(request)
    return redirect(reverse('shop:login'))


#@csrf_exempt
#@csrf_protect
#@login_required
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.all()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	content = {
		'category': category,
		'categories': categories,
		'products': products
	}
	return render(request, "product_list.html", content)



#@csrf_protect
def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug)
	cart_product_form = CartAddProductForm()
	content = {
		'product': product,
		'cart_product_form': cart_product_form
	}
	return render(request, "product_detail.html", content)







