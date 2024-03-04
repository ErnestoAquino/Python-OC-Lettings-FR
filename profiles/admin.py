"""
Registers the Profile model to be managed by the Django admin interface.
"""

from django.contrib import admin
from profiles.models import Profile

# Register your models here.
admin.site.register(Profile)
