from django.contrib import admin
from .models import Suppliers
from .forms import SuppliersSignUpForm as ssp

class SuppliersSignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "username", "price", "date", "logo", "email"]

admin.site.register(Suppliers, SuppliersSignUpAdmin)
# Register your models here.q
