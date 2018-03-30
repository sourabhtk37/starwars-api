from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    # from database.models import Movie, Planet, User
    db.drop_all()
    db.create_all()
