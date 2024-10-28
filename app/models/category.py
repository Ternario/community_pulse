from app import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    questions = db.relationship('Question', backref='category')

    def __repr__(self):
        return f'<Category {self.name}>'
