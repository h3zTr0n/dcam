from django.shortcuts import render
from .models import Supplier
from django.views.generic import DetailView
 
def HomeDisplayView(request):
	 return render(request, "display/home.html", {})
	
# display image data on home page
#class HomeDisplayView(DetailView):
#	template_name = "display/home.html"
#	model_data = Supplier.objects.get()
#	def __init__(self, kwargs):
#		super(HomeDisplayView, self).__init__(kwargs)
#		self.name = model_data.brand_name
#		context = { "supplier": model_data.model_name,
#					"logo": model_data.logo, }
#		suppliers_title = "Welcome to {0}'s".format(self.brand_name)
#		return render(template_name, context)
#	
