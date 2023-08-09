"""Function-based views for profiles app"""
import logging
from django.shortcuts import render
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def profiles_index(request):
    """
    View for the page containing/rendering the profiles list.
    :param request: the user request
    :return: the render function which takes three arguments request, template and context.
    Then it returns a Http Response with the rendered text.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,it.
# Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    View for the page containing/rendering the profile details.
    :param request: the user request
    :param username: the username of the profile we want to consult
    :return: the render function which takes three arguments request, template and context.
    Then it returns a Http Response with the rendered text.
    """

    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profile.html', context)
    except ValueError:
        logging.error("This profile doesn't exist.")

