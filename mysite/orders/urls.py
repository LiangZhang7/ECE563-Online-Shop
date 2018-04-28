from django.urls import include, path
from . import views


app_name = 'orders'
urlpatterns = [
    path('order_create/', views.order_create, name='order_create'),
	path('history/', views.history, name='history'),
]
