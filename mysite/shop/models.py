from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
	category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE,)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id, self.slug])



