from django.shortcuts import url
from .views import SupplierDisplayView as sdv

urlpatterns = [
    url(r'^', sdv.as_view(), name='home'),
]
