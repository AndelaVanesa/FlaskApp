from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField, FileField, SelectField, SelectMultipleField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class ContactForm(FlaskForm):
    name = StringField('Ime',
                        validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    subject = StringField('Naslov',
                        validators=[DataRequired(), Length(min=3, max=20)])
    message = TextAreaField('Poruka',
                        validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField('Pošalji')