"""
This module contains a view to render the home page.

Function:
    - index(request): Renders the home page.
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
