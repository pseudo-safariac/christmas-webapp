from blueprints.main import bp
from flask import render_template


@bp.route('/')
def index()-> str:
    return render_template('index.html', title='Home - Merry Christmas !')
