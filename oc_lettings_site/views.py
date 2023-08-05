"""Function-based views for oc_lettings_site app"""
from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    View for the index page.
    :param request: the user request
    :return: the render function which takes two arguments request and template.
    Then it returns a Http Response with the rendered text.
    """
    return render(request, 'index.html')


def error_404_view(request, exception):
    """Return a custom 404 error page."""
    return render(request, '404.html')


def error_500_view(request):
    """Return a custom 500 error page."""
    return render(request, '500.html')
