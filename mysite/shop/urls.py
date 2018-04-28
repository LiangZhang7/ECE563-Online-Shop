from django.urls import include, path
from . import views

app_name = 'shop'
urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logoutView, name = 'logout'),
	path('product_list/', views.product_list, name = 'product_list'),
	path('product_list/<category_slug>/', views.product_list, name = 'product_list_by_category'),
	path('product_detail/<id>/<slug>/', views.product_detail, name = 'product_detail'),
]
