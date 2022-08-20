# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

from homehub.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User(username='patkennedy79@gmail.com', email='FlaskIsAwesome')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.password_hash != 'FlaskIsAwesome'
    assert user.role == 'user'
