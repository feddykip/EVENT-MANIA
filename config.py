import os

<<<<<<< HEAD
class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY ='5UNFUDgTatqCF-YxSd41Sg'
    
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    
    
=======

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'password'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

>>>>>>> 2c38bc68549c550e73e7b665f4eee9da4fa87299
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
<<<<<<< HEAD
    MAIL_USERNAME = "khalid.serar@student.moringaschool.com"
    MAIL_PASSWORD = "ikmaal855"

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

=======
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://anipherchelsea:Onyango09@localhost/profile'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
>>>>>>> 2c38bc68549c550e73e7b665f4eee9da4fa87299
}