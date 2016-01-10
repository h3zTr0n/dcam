from django.shortcuts import url
# from . import views
from spida.apps.accounts import views

urlpatterns = [
    url(r'^/login/', 'views.LoginView.as_view()', name="Login"),
    url(r'^/logout/', 'views.LogoutView.as_view()', name="Logout" ),
    url(r'^/signup/', 'views.singupView.as_view()', name="signup"),
    url(r'^/passwprdchange', 'views.PasswordChangeView.as_view()', name="change password"),
]
