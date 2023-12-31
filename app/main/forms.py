from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    domain = StringField("Domain", validators=[DataRequired()])
    submit = SubmitField("Submit")
