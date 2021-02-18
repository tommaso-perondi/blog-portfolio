from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class PostCreate(FlaskForm):
    title = StringField('Post title', validators=[DataRequired(), ])
    content = TextAreaField('Post content')
    submit = SubmitField('Create post')
