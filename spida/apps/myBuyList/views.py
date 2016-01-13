from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ShopList(generic.TemplateView):
    template_name = "myBuyList/home.html"

# Method for user shopping list description
class SignUpView(generic.CreateView):
    # form_class = UserCreationForm
    # model = User
    template_name = "myBuyList/signup.html"
