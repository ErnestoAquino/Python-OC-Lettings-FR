"""
Defines URL patterns for the project.

URL Patterns:
    - '/': Maps to the 'index' view.
    - '/lettings/': Includes URL patterns from the 'lettings' application.
    - '/profiles/': Includes URL patterns from the 'profiles' application.
    - '/admin/': Maps to the Django admin interface.
"""

from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
