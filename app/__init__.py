from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_1.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.routers.questions import bp as question_bp
from app.routers.response import bp as response_bp

app.register_blueprint(question_bp)
app.register_blueprint(response_bp)


def create_app():
    # db.init_app(app)
    migrate.init_app(app, db)

    return app
