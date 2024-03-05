import pytest
from django.urls import reverse
from django.urls import resolve

from lettings.models import Address
from lettings.models import Letting
from lettings.views import index as index_view
from lettings.views import letting as letting_view


@pytest.mark.django_db
def test_lettings_index_url():
    """
    Test to verify that the URL of lettings index page resoles correctly
    """
    expected_url = '/lettings/'

    # Use reverse to get the URL from the view name
    url = reverse('lettings:index')

    assert url == expected_url
    assert resolve(url).func == index_view


@pytest.mark.django_db
def test_letting_url():
    """
    Testo to verify that the URL of the letting page resolves correctly
    """
    # Create Letting for testing
    address = Address(number=6,
                      street='Street test',
                      city='City test',
                      state='TT',
                      zip_code=000000,
                      country_iso_code='TES')
    address.save()
    letting = Letting.objects.create(title='Title Test', address=address)

    expected_url = '/lettings/1/'

    # Get the URL for the letting page using reverse with the letting id
    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})

    # Check the URL is as expected
    assert url == expected_url
    assert resolve(url).func == letting_view
