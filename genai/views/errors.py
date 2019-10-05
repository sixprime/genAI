from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException

blueprint = Blueprint('errors', __name__)

@blueprint.app_errorhandler(Exception)
def index(error):
    error_code = 500
    if isinstance(error, HTTPException):
        error_code = error.code
    return render_template('errors/index.html', error=error), error_code
