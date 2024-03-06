import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view_status_code(client):
    """
    Test that the index page can be accessed correctly
    """
    expected_status_code = 200
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == expected_status_code


@pytest.mark.django_db
def test_index_view_uses_correct_template(client):
    """
    Test that the index view uses the correct template.
    """

    expected_template = 'index.html'
    url = reverse('index')
    response = client.get(url)
    templates_used = [t.name for t in response.templates]

    assert expected_template in templates_used
