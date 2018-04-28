from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django import forms
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


def history(request):
    # show transactions history
    orders = Order.objects.filter(user = request.user)
    return render(request, 'order/history.html', {'orders':orders})


def order_create(request):
#of = OrderCreateForm(request.POST)
    cart = Cart(request)
    user = get_object_or_404(User, pk = request.user.id)
    if request.method == 'POST':
        of = OrderCreateForm(request.POST)
        if of.is_valid():
            cd = of.cleaned_data
            email_list =[]
            email_title = "Order Placed in Liang's online shop"
            sender = settings.EMAIL_HOST_USER
            email_content = "Order Placed in Liang's online shop"
            receiver = cd['email']
            email_list.append(receiver)
            send_mail(email_title, email_content, sender, email_list, fail_silently=False)
            order = Order()
            order.user = user
            order.first_name = cd['first_name']
            order.last_name = cd['last_name']
            order.email = cd['email']
            order.home_address = cd['home_address']
            order.zip_code = cd['zip_code']
            order.city = cd['city']
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        of = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'of': of})
