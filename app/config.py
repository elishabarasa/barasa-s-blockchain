# import os

# class Config:
#     # Set the secret key for sessions (you can change this to a secure key)
#     SECRET_KEY = 'ahona'
    
#     # Database configuration
#     # SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/site.db'  # Path to your SQLite database
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@localhost/my_database'

#     SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for performance
class Config:
    # Set the secret key for sessions
    SECRET_KEY = 'ahona'
    
    # Database configuration for Docker
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@db:5432/my_database'

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for performance
