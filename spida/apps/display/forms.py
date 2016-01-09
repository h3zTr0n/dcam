form django import forms
from crispy-froms.layout import Layout, Div, HTML, Field, Submit, Button
from crispy-forms.bootstrap import AppendixText, prependText, formActions
from crispy-forms import 
from crispy-forms.helper import FormHelper
##############################################
class SupplierSignUpForm(authtools.UserSignUpForm):
	def __init__(self, *args, **kwargs):
		super(SupplierSignUpForm, self).__init__(*args, **kwargs)
		self.helper =FormHelper()
		self.layout['email'].widget.input_type = "email"
		self.helpe.layout = Layout(
		Field("email", placeholder="Enter your email", autofocus=""),
		Field("brandname", placeholder="Enter your brand name"),
		# Field("image", placeholder="Enter your username"),
		Field("logo", placeholder="Upload your brand logo here"),
		Field("password1", placeholder="Enter your password"),
		Field("password2", placeholder="Re-enter your password"),
		Submit("Submit", "submit", css_class="btn-warning"),
		)
