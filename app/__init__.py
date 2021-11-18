from flask import Flask
<<<<<<< HEAD
from flask_bootstrap import Bootstrap


app = Flask(__name__)
from app.main import views,forms
app.secret_key = 'EzxToxiYNiDupeWQ8aLpFQ'
bootstrap = Bootstrap()
=======
<<<<<<< HEAD

# Initializing application
app = Flask(__name__)

from app.main import views
=======
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()


def create_app(config_name):

    app = Flask(__name__)

    #Creating application configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    #configure UploadSet
    configure_uploads(app,photos)

    from . auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authentication')

    #Registering the blueprint
    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
>>>>>>> 3c416bbb2737052b6fb177ba277bf5f7f6b20c75
>>>>>>> 2c38bc68549c550e73e7b665f4eee9da4fa87299
