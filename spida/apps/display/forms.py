from django import forms
# from crispy_forms.layout import Layout, Div, HTML, Field, Submit 
# from crispy_forms.bootstrap import AppendedText, PrependedText,FormActions
# from crispy_forms.helper import FormHelper
# from authtools import forms as authtoolsforms
# from .models import Supplier
##############################################

class SupplierSignUpForm(forms.Form):
	brand_name = forms.CharField(max_length=30)
	email = forms.EmailField() 
	price = forms.IntegerField()
	description = forms.CharField(max_length=400)
	date = forms.DateTimeField()
	image = forms.ImageField()
	logo = forms.ImageField()
 