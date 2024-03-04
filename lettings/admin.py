from django.contrib import admin
from lettings.models import Letting
from lettings.models import Address

# Register your models here.
admin.site.register(Letting)
admin.site.register(Address)
