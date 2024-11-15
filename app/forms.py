from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class EditProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[
        DataRequired(),
        EqualTo('password', message='Пароли должны совпадать')
    ])
    submit = SubmitField('Сохранить изменения')

