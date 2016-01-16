from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SupDetails(models.Model):
	supplier_name = models.CharField(max_length=32, blank=False)
	phone_number = models.PositiveIntegerField(blank=False)
	branch_number = models.IntegerField()
	date_joined = models.DateField()

class Food(models.Model):
	food_name = models.CharField(max_length=100, blank=False)
	price = models.PositiveIntegerField(blank=False)
	desciption = models.DateTimeField(max_length=500)
	supplier_name = models.ForeignKey(SupDetails, on_delete=models.CASCADE)
	food_img = models.ImageField()

class Promos(models.Model):
	item_on_promo = models.CharField(max_length=32, blank=False)
	supplier_name = models.ForeignKey(SupDetails, on_delete=models.CASCADE)
	start_date = models.DateTimeField(blank=False)
	end_date = models.DateTimeField(blank=False)
