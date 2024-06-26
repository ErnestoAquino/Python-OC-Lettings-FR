"""
This module contains views for the lettings application.

It provides views to display a list of all available lettings on the index page and to show the
details of a specific letting selected by the user. The view functions use the Letting model to
retrieve information from the database and pass it to the corresponding templates for presentation.

Functions:
    - index(request): Displays the index page with a list of all lettings.
    - letting(request, letting_id): Displays the details of a specific letting.
"""
import logging
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseServerError

from .models import Letting

logger = logging.getLogger('django')


# Create your views here. Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis
# velit. Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras
# eget scelerisque
def index(request):
    """
    Display a list of lettings on the index page.

    This view retrieves all letting objects from the database and passes them to the index template
    to display a list of lettings.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered index page with the lettings list.
    """
    try:
        # Attempt to retrieve all letting objects from the database
        lettings_list = Letting.objects.all()
    except Exception as e:
        # Log the error
        logger.error('Error retrieving lettings from database: %s', e)
        return HttpResponseServerError('Internal Server Error')

    # Prepare context data to pass to the template
    context = {'lettings_list': lettings_list}

    # Render the index page with the lettings list
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas
# auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna.
# Suspendisse potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan
# interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique
# mauris eu velit fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi
# ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Display details of a specific letting.

    This view retrieves the letting object with the given letting_id from the database
    and passes its title and address to the letting template display the letting details.

    Args:
        request (HttpRequest): The HTTP request.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered letting page with the letting details.
    """
    # Use get_object_or_404 to automatically raise Http404 if the object is not found
    letting_instance = get_object_or_404(Letting, id=letting_id)

    # Prepare context data with letting details
    context = {
        'title': letting_instance.title,
        'address': letting_instance.address,
    }

    # Render the letting page with the letting details
    return render(request, 'lettings/letting.html', context)
