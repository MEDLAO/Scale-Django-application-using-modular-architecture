
def test_profile_model(profiles_fixture):

    """
    Testing whether Profile's __str__ method is implemented properly
    """
    user_obj, profile_obj = profiles_fixture

    expected_value = profile_obj.user.username
    assert str(profile_obj) == expected_value
