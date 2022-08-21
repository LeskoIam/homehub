# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import pytest
from homehub_web.app import db
from homehub_web.models import User

import logging

log = logging.getLogger(__name__)


# @pytest.fixture(scope='module')
# def new_user():
#     user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
#     return user


@pytest.fixture(scope='module')
def init_database():
    log.info(f"Creating test database {db=}")
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(username="test-user1", email="test@user.com")
    user1.set_password("password")
    user2 = User(username="test-user2", email='test-2@user.com', role="admin")
    user2.set_password('PaSsWoRd')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    log.info("Dummy users created, ready for testing")

    yield  # this is where the testing happens!

    log.info(f"Dropping test database {db=}")
    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)
