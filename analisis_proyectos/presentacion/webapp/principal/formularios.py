from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class NombreForm(FlaskForm):
    nombre = StringField("Cual es tu nombre?", [validators.DataRequired()])
    submit = SubmitField("Aceptar")