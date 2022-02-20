from tkinter import Widget
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
#from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    msg = StringField('Message', validators=[DataRequired()])