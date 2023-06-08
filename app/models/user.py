from app.extensions import db

class Users(db.Model):
    username = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def serialize(self): 
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }