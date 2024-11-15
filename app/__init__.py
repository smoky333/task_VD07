from flask import Flask
from flask_bootstrap import Bootstrap4

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    Bootstrap4(app)

    # Регистрация Blueprint
    from .routes import main
    app.register_blueprint(main)

    return app


