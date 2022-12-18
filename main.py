from flask import Flask

from config import Config
from extensions import db
from flask_wtf.csrf import CSRFProtect

from blueprints.main.routes import bp as main_index


def create_app(config_class=Config) -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Configurations
    app.secret_key='1970ddb5848934a411c4def036b68a4e3019a45d79c5d1b9d9553564522f9c8b'

    # Create the blueprint db
    with app.app_context():
        db.create_all()

    # Register blueprints here
    app.register_blueprint(main_index)
    
    @app.route('/test/')
    def test_page()-> str :
        """try:
            db.session.query(text('1')).from_statement(text('SELECT 1')).all()
            return '<h1>it works!</h1>'
        except Exception as e:
            error_text = f'<p> The Error:<br> {e}</p>'
            header = '<h1>Something is wrong!</h1>'
            return header+error_text"""
        return 'The app is Functional'

    return app



if __name__ == '__main__':
	create_app().run(host="0.0.0.0", port=5000, debug=True)