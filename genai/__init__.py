from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)

    with app.app_context():
        # Register blueprints
        from .views import home
        app.register_blueprint(home.blueprint)

        from .views import errors
        app.register_blueprint(errors.blueprint)

        return app
