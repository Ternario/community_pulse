from app import db
from datetime import datetime
from .category import Category


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    responses = db.relationship("Responses", backref='question')
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    questions = db.relationship('Questions', backref='category', cascade='all, delete-orphan')

    def __str__(self):
        return f"Question: {self.text}"
