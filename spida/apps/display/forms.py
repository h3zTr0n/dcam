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

	
#class SupplierSignUpForm(authtoolsforms):
#	def __init__(self, *args, **kwargs):
#		super(SupplierSignUpForm, self).__init__(*args, **kwargs)
#		self.helper = FormHelper()
#		self.layout['email'].widget.input_type = "email"
#		self.helpe.layout = Layout(
#		Field("email", placeholder="Enter your email", autofocus=""),
#		Field("brandname", placeholder="Enter your brand name"),
#		# Field("image", placeholder="Enter your username"),
#		# Field("password1", placeholder="Enter your password"),
#		# Field("password2", placeholder="Re-enter your password"),
#		Submit("Submit", "submit", css_class="btn-warning"),
#		)
