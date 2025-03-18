from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    name_complete = StringField("Name Complete", validators=[DataRequired(), Length(min=8, max=100)])
    nameuser = StringField("Username", validators=[DataRequired(), Length(min=3, max=35)])
    email = StringField("Email", validators=[DataRequired(), Email()])  # Corrigido de 'Email' para 'email'
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=35)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=35)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=35)])
