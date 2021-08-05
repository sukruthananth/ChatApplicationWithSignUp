from datetime import datetime
from . import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(150))
    name = db.Column(db.String(150) )
    password = db.Column(db.String(150))
    time = db.Column(db.DateTime, default= datetime.now)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1500))
    user_name = db.Column(db.String(150))
    time = db.Column(db.DateTime, default=datetime.now)