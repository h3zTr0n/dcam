from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Model for the supplier

class Supplier(models.Model):
    brand_name = models.CharField(max_length=30)
    email = models.EmailField()
    price = models.IntegerField()
    description = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d")
    logo = models.ImageField()

    class Meta:
        abstract = False

# @python_2_unicode_compatible
class Supp(Supplier):

    def __unicode__(self):
        return "{}'s' profile". format(self.brand_name)
