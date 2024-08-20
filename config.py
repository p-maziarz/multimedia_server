import os 

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/db_name')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')