import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/eventmania'
    #UPLOADED_PHOTOS_DEST ='app/static/photos'

    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY ='5UNFUDgTatqCF-YxSd41Sg'
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '236d1ffbf7aa6933f300c626273e39ed'
    #SQLALCHEMY_TRACK_MODIFICATIONS=False
    #  email configurations
    #MAIL_SERVER = 'smtp.googlemail.com'
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = "khalid.serar@student.moringaschool.com"
    #MAIL_PASSWORD = "ikmaal855"

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
    #    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)
    pass
    

    #@staticmethod
    #def init_app(app):
    #    pass


class TestConfig(Config):
    pass



class DevConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/events'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}