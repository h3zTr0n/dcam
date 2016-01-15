from __future__ import absolute_import

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm

# Create your views here.

class ShopListView(generic.TemplateView):
    template_name = "shopList/shop.html"

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    user = User
    template_name = "accounts/signup.html"

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = "accounts/login.html"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data.get['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
