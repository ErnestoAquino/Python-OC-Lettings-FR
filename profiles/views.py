"""
This module contains views for the profiles application.

It provides views to display a list of all profiles on the index page and to show the details
of a specific profile selected by the user. The view functions use the Profile model to retrieve
information from the database and pass it to the corresponding templates for presentation.

Functions:
    - index(request): Displays the index page with a list of all profiles.
    - profile(request, username): Displays the details of a specific profile.
"""

import logging
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseServerError
from .models import Profile

logger = logging.getLogger('django')


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    Display a list of profiles.

    This view retrieves all profile objects from the database and passes them
    to the index template to display a list of profiles.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered index page with the list of profiles.
    """
    try:
        # Attempt to retrieve  all profile objects from the database
        profiles_list = Profile.objects.all()
    except Exception as e:
        # Log the error
        logger.error('Error retrieving profiles from database: %s', e)
        return HttpResponseServerError('Internal Server Error')

    # Prepare context data with profiles list
    context = {'profiles_list': profiles_list}

    # Render the index page with the list of profiles
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis
# fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males
def profile(request, username):
    """
    Display a profile detail page.

    This view retrieves a specific profile object from the database based on
    the provided username, and passes it to the profile template to display
    detailed information about the profile.

    Args:
        request (HttpRequest): The HTTP request.
        username (str): The username associated with the profile.

    Returns:
        HttpResponse: The rendered profile page with detailed profile information.
    """
    # Using 'get_object_or_404' to automatically handle the case of profile is not found
    profile_instance = get_object_or_404(Profile, user__username=username)

    # Prepare context data with the profile instance
    context = {'profile': profile_instance}

    # Render the profile page with detailed profile information
    return render(request, 'profiles/profile.html', context)
