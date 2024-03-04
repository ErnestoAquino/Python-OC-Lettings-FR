"""
Registers the Letting and Address models to be managed by the Django admin interface.
"""

from django.contrib import admin
from lettings.models import Letting
from lettings.models import Address

# Register your models here.
admin.site.register(Letting)
admin.site.register(Address)
