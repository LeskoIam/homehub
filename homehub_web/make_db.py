# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

from homehub_web import db
from homehub_web.models import User
db.create_all()

user = User(username="admin", email="admin@admin.com", role="admin")
user.set_password("admin")
db.session.add(user)

# Commit the changes for the users
db.session.commit()
