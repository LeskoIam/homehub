# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be awhile before you realize something's wrong.

from flask.cli import FlaskGroup

from homehub_web import app, db
# from homehub_web.models import User


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# @cli.command("seed_db")
# def seed_db():
#     db.session.add(User(email="michael@mherman.org"))
#     db.session.commit()


if __name__ == "__main__":
    cli()
