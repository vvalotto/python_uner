from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import principal
from .formularios import NombreForm


@principal.route('/', methods=['GET', 'POST'])
def index():
    form = NombreForm()
    if form.validate_on_submit():
        session['nombre'] = form.nombre.data
        return redirect(url_for('.index'))

    return render_template('index.html', form=form,
                            nombre=session.get('nombre'))
