from __future__ import absolute_import

from django.views import generic
from django.contrib.auth.models import User
from .forms import RegistrationForm

# Create your views here.

class ShopListView(generic.TemplateView):
    template_name = "shopList/shop.html"

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    user = User
    template_name = "accounts/signup.html"
