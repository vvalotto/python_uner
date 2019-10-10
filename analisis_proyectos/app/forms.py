from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')


class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')


class ModuloForm(FlaskForm):
    nombre = StringField('Modulo', validators=[DataRequired(), Length(max=128)])

class ListaProyectoForm(FlaskForm):
    lista_proyectos = []

    @staticmethod
    def inicializar():
        ListaProyectoForm.lista_proyectos = []

class ProyectoForm(FlaskForm):
    nombre_proyecto = StringField('Nombre del Proyecto', validators=[DataRequired(), Length(max=50)])
    descripcion = StringField('Descripcion')
    lista_modulos = []

    @staticmethod
    def inicializar():
        ProyectoForm.nombre_proyecto = None
        ProyectoForm.descripcion = None
        ProyectoForm.lista_modulos = []

class ComponenteForm(FlaskForm):
    nombre_componente = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    tipo = StringField('Tipo')
    lista_elementos = []

    @staticmethod
    def inicializar():
        ComponenteForm.nombre_componente = None
        ComponenteForm.tipo = None
        ComponenteForm.lista_elementos = []
