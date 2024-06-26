import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.utils import OperationalError
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view_status_code(client):
    """
    Test that the index page can be accessed correctly
    """
    expected_status_code = 200
    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == expected_status_code


@pytest.mark.django_db
def test_index_view_uses_correct_template(client):
    """
    Test that the index view uses the correct template
    """
    expected_template = 'profiles/index.html'
    url = reverse('profiles:index')
    response = client.get(url)
    templates_used = [t.name for t in response.templates]

    assert expected_template in templates_used


@pytest.mark.django_db
def test_index_view_context_data(client):
    """
    Test that the index view include the list of profiles in the context.
    """

    # Create test user and profile
    user = User.objects.create_user(username='test_user', password='test_password123')
    Profile.objects.create(user=user, favorite_city='Test City')

    expected_len_of_list = 1
    url = reverse('profiles:index')
    response = client.get(url)

    # Check if 'profiles_list' is in the context and has the expected len
    assert 'profiles_list' in response.context
    assert len(response.context['profiles_list']) == expected_len_of_list


@pytest.mark.django_db
def test_index_view_with_no_profiles(client):
    """
    Test that the index view handles the case when there are no profiles.
    """

    expected_len_of_list = 0
    url = reverse('profiles:index')
    response = client.get(url)

    # Check if 'profiles_list' is int the context and empty
    assert 'profiles_list' in response.context
    assert len(response.context['profiles_list']) == expected_len_of_list


@pytest.mark.django_db
def test_profile_index_view_database_error(mocker, client):
    """
    Test that the index view returns a server error response when a database error occurs
    """
    mock_logger_error = mocker.patch('logging.Logger.error')

    # 'Mock' the 'all()' method
    mocker.patch.object(Profile.objects, 'all', side_effect=OperationalError)

    # Make a GET request to the 'index' view
    url = reverse('profiles:index')
    response = client.get(url)

    # Check that a server error response is returned
    assert response.status_code == 500
    mock_logger_error.assert_called()


@pytest.mark.django_db
def test_index_view_contains_three_profiles(client):
    """
    Test that the index view displays exactly three profiles with their usernames.
    """

    # Create 3 user and profiles for test
    usernames = ['user1', 'user2', 'user3']
    for username in usernames:
        user = User.objects.create_user(username=username, password='test_password123')
        Profile.objects.create(user=user, favorite_city='Test City')

    expected_number_of_profiles = 3
    url = reverse('profiles:index')
    response = client.get(url)

    # Check that the length of the profiles list is 3
    assert len(response.context['profiles_list']) == expected_number_of_profiles

    # Check that the usernames are displayed in the template
    for username in usernames:
        expected_string = f'href="/profiles/{username}/">{username}</a>'
        assert expected_string in response.content.decode()


@pytest.mark.django_db
def test_profile_view_status_code(client):
    """
    Test that the profile detail page can be accessed correctly for an existing profile.
    """
    # Create test user and profile
    user = User.objects.create_user(username='test_user', password='test_password123')
    Profile.objects.create(user=user, favorite_city='Test City')

    url = reverse('profiles:profile', kwargs={'username': 'test_user'})
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_uses_correct_template(client):
    """
    Test that the profile view uses the correct template.
    """

    expected_template = 'profiles/profile.html'
    user = User.objects.create_user(username='testuser2', password='testpassword123')
    Profile.objects.create(user=user, favorite_city='Another City')

    url = reverse('profiles:profile', kwargs={'username': 'testuser2'})
    response = client.get(url)

    templates_used = [t.name for t in response.templates]
    assert expected_template in templates_used


@pytest.mark.django_db
def test_profile_view_context_data(client):
    """
    Test that the profile view includes the correct profile instance in the context.
    """
    # Create test user and profile
    user = User.objects.create_user(username='test_user3', password='test_password123')
    expected_city = 'Cool City'
    Profile.objects.create(user=user, favorite_city=expected_city)

    url = reverse('profiles:profile', kwargs={'username': 'test_user3'})
    response = client.get(url)

    # Check if 'profile' is in the context and has the correct data
    profile_instance = response.context['profile']
    assert profile_instance.user.username == 'test_user3'
    assert profile_instance.favorite_city == expected_city


@pytest.mark.django_db
def test_profile_view_with_nonexistent_username(mocker, client):
    """
    Test that the profile view returns a 404 error for a nonexistent username.
    """
    mock_logger_error = mocker.patch('logging.Logger.error')

    expected_status_code = 404
    url = reverse('profiles:profile', kwargs={'username': 'nonexistent'})
    response = client.get(url)

    assert response.status_code == expected_status_code
    mock_logger_error.assert_called()
