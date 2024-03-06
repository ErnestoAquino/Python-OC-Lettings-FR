import pytest
from django.urls import reverse
from django.db.utils import OperationalError

from lettings.models import Address
from lettings.models import Letting


@pytest.mark.django_db
def test_letting_index_status_code(client):
    """
    Test that the lettings index page can be accessed correctly,
    """
    expected_status_code = 200
    url = reverse('lettings:index')
    response = client.get(url)

    assert response.status_code == expected_status_code


@pytest.mark.django_db
def test_lettings_index_view_uses_correct_template(client):
    """
    Test that the index lettings view uses the correct template.
    """
    expected_template = 'lettings/index.html'
    url = reverse('lettings:index')
    response = client.get(url)
    templates_used = [t.name for t in response.templates]

    assert expected_template in templates_used


@pytest.mark.django_db
def test_letting_index_view_context_data(client):
    """
    Test that the index letting view include the list of lettings in the context.
    """
    # Create test letting
    address = Address(number=6,
                      street='Street test',
                      city='City test',
                      state='TT',
                      zip_code=000000,
                      country_iso_code='TES')
    address.save()
    Letting.objects.create(title='Title Test', address=address)

    expected_len_of_list = 1
    url = reverse('lettings:index')
    response = client.get(url)

    # Check if 'lettings_list' is in the context and has the expected len
    assert 'lettings_list' in response.context
    assert len(response.context['lettings_list']) == expected_len_of_list


@pytest.mark.django_db
def test_letting_index_view_no_lettings(client):
    """
    The that the letting index view handles the case when there are no lettings.
    """
    expected_len_of_list = 0
    url = reverse('lettings:index')
    response = client.get(url)

    # Check if 'lettings_list' is in the context and empty
    assert 'lettings_list' in response.context
    assert len(response.context['lettings_list']) == expected_len_of_list


@pytest.mark.django_db
def test_index_view_contains_three_lettings(client):
    """
    Test that the index view displays exactly three lettings with their titles.
    """

    # Create 3 addresses and lettings for the test
    titles = ['Letting 1', 'Letting 2', 'Letting 3']
    for title in titles:
        address = Address.objects.create(number=123, street="Main Street",
                                         city="Anytown", state="AN", zip_code=12345,
                                         country_iso_code="ATC")
        Letting.objects.create(title=title, address=address)

    expected_number_of_lettings = 3
    url = reverse('lettings:index')
    response = client.get(url)

    # Check that the length of the lettings list is 3
    assert len(response.context['lettings_list']) == expected_number_of_lettings

    # Check that the titles are displayed in the template
    for title in titles:
        expected_string = f'>{title}</a>'
        assert expected_string in response.content.decode()


@pytest.mark.django_db
def test_lettings_index_view_database_error(mocker, client):
    """
    Test that the letting index view returns a server error response when a database error occurs
    """

    # 'Mock' the 'all()' method
    mocker.patch.object(Letting.objects, 'all', side_effect=OperationalError)

    # Make a GET request to the 'index'
    url = reverse('lettings:index')
    response = client.get(url)

    # Check that the server error response is returned
    assert response.status_code == 500


@pytest.mark.django_db
def test_letting_view_status_code(client):
    """
    Test that the letting detail page can be accessed correctly for an existing letting
    """
    expected_status_code = 200

    # Create letting
    address = Address(number=6,
                      street='Street test',
                      city='City test',
                      state='TT',
                      zip_code=000000,
                      country_iso_code='TES')
    address.save()
    letting = Letting.objects.create(title='Title Test', address=address)

    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    assert response.status_code == expected_status_code


@pytest.mark.django_db
def test_letting_view_uses_correct_template(client):
    """
    Test that the letting view uses the correct template.
    """

    expected_template = 'lettings/letting.html'
    address = Address(number=6,
                      street='Street test',
                      city='City test',
                      state='TT',
                      zip_code=000000,
                      country_iso_code='TES')
    address.save()
    letting = Letting.objects.create(title='Title Test', address=address)

    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    templates_used = [t.name for t in response.templates]
    assert expected_template in templates_used


@pytest.mark.django_db
def test_letting_view_context_data(client):
    """
    Test that the letting view includes the correct letting instance in the context.
    """

    # Create letting
    address = Address(number=6,
                      street='Street test',
                      city='City test',
                      state='TT',
                      zip_code=000000,
                      country_iso_code='TES')
    address.save()
    letting = Letting.objects.create(title='Title Test', address=address)

    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    # Check if 'title' and 'address' are in the context and have the correct data
    assert response.context['title'] == 'Title Test'
    assert response.context['address'] == address


@pytest.mark.django_db
def test_letting_view_with_nonexistent_letting_id(client):
    """
    Test that the profile view returns a 404 error for nonexistent letting
    """

    expected_status_code = 404
    url = reverse('lettings:letting', kwargs={'letting_id': 100})
    response = client.get(url)

    assert response.status_code == expected_status_code
