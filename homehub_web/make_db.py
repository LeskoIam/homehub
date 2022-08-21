# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

try:
    from app import db
    print("1")
except ImportError:
    print("No")

try:
    from homehub_web.app import db
    print("2")
except ImportError:
    print("No")

try:
    from . import db
    print("3")
except ImportError:
    print("No")

try:
    import db
    print("4")
except ImportError:
    print("No")

try:
    import app.db as db
    print("5")
except ImportError:
    print("No")

try:
    import homehub_web.app.db as db
    print("6")
except ImportError:
    print("No")

from models import User
db.create_all()

user = User(username="admin", email="admin@admin.com", role="admin")
user.set_password("admin")
db.session.add(user)

# Commit the changes for the users
db.session.commit()
