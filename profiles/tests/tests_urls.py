import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import resolve
from profiles.models import Profile
from profiles.views import profile as profile_view
from profiles.views import index as index_view


@pytest.mark.django_db
def test_index_url():
    """
    Test to verify that the URL of the index page resolves correctly.
    """
    expected_url = '/profiles/'

    # Use reverse to get the URL from the view name
    url = reverse('profiles:index')

    # Verify that the obtained URL is equal to the expected one
    assert url == expected_url
    assert resolve(url).func == index_view


@pytest.mark.django_db
def test_profile_url():
    """
    Test to verify that the URL of the profile page resolves correctly.
    """
    # Create a user and profile for testing
    user = User.objects.create_user(username='test_user', password='test_password123')
    Profile.objects.create(user=user, favorite_city='Test City')
    expected_url = '/profiles/test_user/'

    # Get the URL for the profile page using reverse with the username
    url = reverse('profiles:profile', kwargs={'username': 'test_user'})

    # Use resolve to find out which view is supposed to handle that URL
    # and verify that it is the expected view function (profile_view)
    assert url == expected_url
    assert resolve(url).func == profile_view
