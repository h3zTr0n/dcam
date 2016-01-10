from django.contrib import admin
from .models import Supplier
from .forms import SupplierSignUpForm as ssp

# class SupplierSignUpAdmin(admin.ModelAdmin):
#    list_display = ["__unicode__", "username", "price", "date", "logo", "email"]

admin.site.register(Supplier)
# Register your models here.q
