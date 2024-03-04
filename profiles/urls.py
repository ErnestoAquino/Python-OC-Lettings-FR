"""
Defines URL patterns for the 'profiles' application.

URL Patterns:
    - '/': Maps to the 'index' view, displaying a list of all profiles.
    - '/<str:username>/': Maps to the 'profile' view, displaying details of a specific profile.
"""


from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
