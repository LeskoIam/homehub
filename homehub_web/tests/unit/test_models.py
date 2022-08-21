# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import logging

from homehub_web.models import User
from homehub_web import app
from homehub_web.config import TestConfig

app.config.from_object(TestConfig)

log = logging.getLogger(__name__)


def test_new_user(init_database):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User.query.filter_by(username="test-user1").first()
    assert user.password_hash != 'password', "Password is in plain text!"
    assert user.role == 'user', f"Wrong user role. Expected 'user' got '{user.role}'"
