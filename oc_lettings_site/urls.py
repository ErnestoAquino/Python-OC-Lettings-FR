"""
Defines URL patterns for the project.

URL Patterns:
    - '/': Maps to the 'index' view.
    - '/lettings/': Includes URL patterns from the 'lettings' application.
    - '/profiles/': Includes URL patterns from the 'profiles' application.
    - '/admin/': Maps to the Django admin interface.

Additionally, custom handlers for error pages are defined to provide a better user experience for
HTTP 404 and 500 errors.

Attributes:
    urlpatterns (list): A list of `path` instances that maps URLs to views.
    handler404 (str): The path to the view function for handling 404 errors.
    handler500 (str): The path to the view function for handling 500 errors.
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import handler404
from django.conf.urls import handler500

from . import views

# URL configuration for the site, mapping URLs to views.
urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),  # Django admin site
]

# Custom error handlers
handler404 = 'oc_lettings_site.views.error_404'  # noqa: F811
handler500 = 'oc_lettings_site.views.error_500'  # noqa: F811
