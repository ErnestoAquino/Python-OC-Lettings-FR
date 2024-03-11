"""
This module contains a view to render the home page.

Function:
    - index(request): Renders the home page.
    - error_404(request, exception): Renders a custom 404 error page.
    - error_500(request): Renders a custom 500 error page.
"""

from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam
# vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim
# cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Renders the home page.

    Parameters:
    - request: The HTTP request received by the server.

    Returns:
    - An HTTP response rendering the 'index.html' template.
    """
    return render(request, 'index.html')


def error_404(request, exception):
    """
    Renders a custom 404 error page.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - exception (Exception): The exception that caused the 404 error.

    Returns:
    - HttpResponse: The response object with the rendered '404.html' template and 404 status code.
    """
    return render(request, '404.html', {}, status=404)


def error_500(request):
    """
    Renders a custom 500 error page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The response object with the rendered '500.html' template and 500 status code.
    """
    return render(request, '500.html', {}, status=500)
