from flask import Blueprint

bp: Blueprint = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path='/static')

from blueprints.main import routes
