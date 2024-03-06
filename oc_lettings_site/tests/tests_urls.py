import pytest
from django.urls import reverse
from django.urls import resolve

from oc_lettings_site.views import index as index_view


@pytest.mark.django_db
def test_home_index_url():
    """
    Test to verify that the URL of home index page resolves correctly.
    """

    expected_url = '/'

    # Use reverse to get the URL
    url = reverse('index')

    assert url == expected_url
    assert resolve(url).func == index_view
