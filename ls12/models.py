from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(50), nullable=False)



