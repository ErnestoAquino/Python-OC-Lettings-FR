import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_creation():
    """
    Test the creation and retrieval of a Profile instance
    """
    # Create user and profile
    user = User.objects.create_user(username='test_user', password='test_password123')
    Profile.objects.create(user=user, favorite_city='Test City')

    # Retrieve the profile from the database
    retrieved_profile = Profile.objects.get(user__username='test_user')

    # Check the profile's attributes
    assert retrieved_profile.user == user
    assert retrieved_profile.favorite_city == 'Test City'


@pytest.mark.django_db
def test_profile_str_method():
    """
    Test the __str__ method of the Profile
    """
    # Create user and profile
    user = User.objects.create_user(username='test_user', password='test_password123')
    profile = Profile.objects.create(user=user, favorite_city='Test City')

    assert str(profile) == 'test_user'
