from django.shortcuts import render
from .models import Suppliers
from django.views.generic import DetailView


class DisplaySupplierView(DetailView):
    template_name = "display/display/"
    obj_name = Suppliers.objects.get()

    def show_content_on_page(self, *args, **kwargs):
        super(DisplaySupplierView, self).__init__(*args, kwargs)
        for item in obj_name:
            if item == 'username':
                return item

        context = {"logos": obj_name}
        supplier_title = " Welcome to {0}". format(item)
        return  render(template_name, context)
