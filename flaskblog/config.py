import os

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY') 
    SECRET_KEY = 'd1977121aa0c44c245afcb47d5268264'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:10141992@localhost/flaskwebapp'
    DATABASE_URL = 'postgres://ymomattahygpyd:4d4740cb9cf8531e41f0d2fd38b00839a7d5844d191865329ede40c7a74ae1e6@ec2-18-214-214-252.compute-1.amazonaws.com:5432/d6hgutmgbd82ag'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
