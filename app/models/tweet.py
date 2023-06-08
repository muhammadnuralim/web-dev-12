from app.extensions import db

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))

    def serialize(self): 
        return {
            "id": self.id,
            "content": self.content
        }
    
