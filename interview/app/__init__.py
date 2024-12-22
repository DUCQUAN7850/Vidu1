from flask import Flask
from app.database import db
from app.auth.routes import auth_bp
from app.comments.routes import comments_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(comments_bp, url_prefix="/comments")

    with app.app_context():
        db.create_all()  # Create tables if not exists

    return app
