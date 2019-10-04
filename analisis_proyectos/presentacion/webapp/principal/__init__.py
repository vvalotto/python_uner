from flask import Blueprint

principal = Blueprint('principal', __name__)

from . import vistas, errores

