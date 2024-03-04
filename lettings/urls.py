"""
Defines URL patterns for the 'lettings' application.

URL Patterns:
    - '/': Maps to the 'index' view, displaying a list of all lettings.
    - '/<int:letting_id>/': Maps to the 'letting' view, displaying details of a specific letting.
"""


from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
