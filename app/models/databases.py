"""import app
from flask_sqlalchemy import SQLAlchemy
from os import environ
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DB_URL")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename_ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)

    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username

    #def json(self):
        #return {"id": id, "username": username, "email": email}



db.create_all()"""