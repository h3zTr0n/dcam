from django.conf.urls import url
from .views import HomeDisplayView as hdv
 
urlpatterns = [
    url(r'^', hdv, name='home'),
]
