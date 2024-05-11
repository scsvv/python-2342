from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.secret_key = '12345123121'

admin = Admin(app)
db = SQLAlchemy()
migrate = Migrate(app, db)

class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

    articles = db.relationship('Article', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"{self.surname}"

class Article(db.Model):
    __tablename__ = 'article'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    img = db.Column(db.String(130), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


    def __repr__(self) -> str:
        return f"Article '{self.title}'"


admin.add_view(ModelView(Article, db.session))
admin.add_view(ModelView(Author, db.session))

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article_page(article_id):
    article = Article.query.get(article_id)
    if article:
        return render_template('article.html', article=article)
    else:
         return render_template('notfounded.html')


if __name__ == "__main__":
    app.run(debug=True)