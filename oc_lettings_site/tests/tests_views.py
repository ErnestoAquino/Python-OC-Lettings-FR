import pytest
from django.test import RequestFactory
from django.core.exceptions import PermissionDenied
from django.urls import reverse

from oc_lettings_site.views import error_404
from oc_lettings_site.views import error_500


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


@pytest.mark.django_db
def test_custom_404_view(mocker):
    """
    Test that the custom 404 view logs the error.
    """

    request_factory = RequestFactory()
    request = request_factory.get('/path-that-does-not-exist')
    exception = PermissionDenied('This is a test exception')

    mock_logger = mocker.patch('logging.Logger.error')

    response = error_404(request, exception)

    mock_logger.assert_called_once_with(f"404 error: {request.path} caused by {exception}")
    assert response.status_code == 404


@pytest.mark.django_db
def test_custom_500_view_renders_correct_template():
    """
    Test that the custom 500 error view renders the correct template.
    """

    request_factory = RequestFactory()
    request = request_factory.get('/some-path')

    response = error_500(request)

    assert response.status_code == 500
    assert 'Sorry, an internal error has occurred' in response.content.decode()
