import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True