# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import pytest
import logging

from homehub_web.app import app
from homehub_web.config import TestConfig

app.config.from_object(TestConfig)

log = logging.getLogger(__name__)


@pytest.mark.parametrize("page,expected,args", [("/", 200, None),
                                                ("/why", 401, None),
                                                ("/abcde45kg", 404, None),
                                                ("/login", 200, ["Username", "Password", "Remember Me"])])
def test_pages_user_logged_out(page, expected, args):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get(page)
        assert response.status_code == expected
        if args is not None:
            for arg in args:
                log.info(f"Testing {page=} for {arg=}")
                assert arg.encode("utf-8") in response.data
