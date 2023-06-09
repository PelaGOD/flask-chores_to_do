from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


class TodoForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('create') 

class DeleteTodoForm(FlaskForm):
    SubmitField = SubmitField('Delete')


class UpdateTodoForm(FlaskForm):
    SubmitField = SubmitField('Update')