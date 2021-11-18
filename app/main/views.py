from flask import render_template,request,redirect,url_for,abort
from . import main
import urllib.request,json
#import requests
from ..models import Event, User
from .forms import EventForm, ContactForm, UpdateProfile
from .. import db,photos
from os import uname
from flask_login import login_required,current_user


@main.route('/events',methods=['GET','POST'])    
def events():
    event_form = EventForm()
    if event_form.validate_on_submit():
        new_event = Event(name = event_form.name.data, day = event_form.day.data, location = event_form.location.data,price = event_form.price.data, owner = event_form.owner.data )
        db.session.add(new_event)
        db.session.commit()
        

    return render_template('events.html', event_form = event_form)

@main.route('/newly-posted',methods=['GET','POST'])    
def recent():
    
    try:
        events = Event.query.all()
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

    return render_template('recent.html', events = events)

@main.route('/contactus', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        # res = pd.DataFrame({'name': name, 'email': email, 'subject': subject, 'message': message}, index=[0])
        # res.to_csv('./contactusMessage.csv')
        return render_template('contact.html', form=form)


@main.route('/')
def home():

    return render_template('index.html')
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
