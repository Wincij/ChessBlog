import os

class Config:
    SECRET_KEY = '66d4319be3000c0b2e975b48d113347b3815d92a5ba76b3bde6fe4e44757d38b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
