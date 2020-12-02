from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Enter a valid email.")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

class PostCreate(FlaskForm):
    title = StringField('Post title', validators=[DataRequired(),])
    content = TextAreaField('Post content')
    submit = SubmitField('Create post')