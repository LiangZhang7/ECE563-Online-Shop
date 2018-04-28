from django import forms
from django.utils import timezone
from .models import Order
from django.forms import ModelForm


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
#exclude = ['created', 'updated']
        fields = ['first_name', 'last_name', 'email', 'home_address', 'zip_code', 'city']

'''
class OrderCreateForm(forms.Form):
'''
