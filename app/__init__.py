from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
from app.main import views,forms
app.secret_key = 'EzxToxiYNiDupeWQ8aLpFQ'
bootstrap = Bootstrap()
