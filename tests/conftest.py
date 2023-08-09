import pytest
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


@pytest.fixture
def lettings_fixture(db):
    address_obj = Address.objects.create(
        number=1234,
        street='address_test',
        city='city_test',
        state='state_test',
        zip_code=12345,
        country_iso_code=123
    )
    letting_obj = Letting.objects.create(
        title='title_test',
        address=address_obj
    )
    return address_obj, letting_obj


@pytest.fixture
def profiles_fixture(db):
    user_obj = User.objects.create(
        username='username_test',
        password='password_test'
    )
    profile_obj = Profile.objects.create(
        user=user_obj,
        favorite_city='favorite_city_test'
    )

    return user_obj, profile_obj
