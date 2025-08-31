from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Adv(db.Model):
    __tablename__ = 'adv'

    id = db.Column(db.Integer, primary_key=True)    
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Adv {self.title}>'
