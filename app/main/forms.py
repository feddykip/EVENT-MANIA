from flask_wtf import FlaskForm 
from wtforms import SelectField,StringField,SubmitField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')



class ContactForm(FlaskForm):
    name = TextAreaField("Name")
    email = TextAreaField("Email")
    subject = TextAreaField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")    


class EventForm(FlaskForm):
    name = StringField('Enter name of event')
    day = StringField('Enter day of event')
    #time = StringField('Enter time of event')
    location = StringField('Enter location with Nairobi')
    owner = StringField('Enter name of event owner/ticketing manager')
    price = StringField('Enter you charges')
    submit = SubmitField('Submit') 
