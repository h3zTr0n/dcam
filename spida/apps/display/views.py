from django.shortcuts import render
from .models import Supplier
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required


def HomeDisplayView(request):
    template_name = "display/home.html"
    items = Supplier.objects.all().order_by('-id')
    context = {'items': items}
    return render(request, template_name, context)

     
