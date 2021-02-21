from flask import Blueprint, render_template
from auth import parentdir
import os

errors = Blueprint('errors', __name__, template_folder=os.path.join(parentdir,"templates/errors"))


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('404.html'), 500
