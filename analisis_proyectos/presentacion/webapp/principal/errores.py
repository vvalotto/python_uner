from flask import render_template
from . import principal

@principal.errorhandler(404)
def pagina_no_encontrad(e):
    return render_template('404.html'), 404

@principal.errorhandler(500)
def error_server(e):
    return render_template('500.html'), 500
