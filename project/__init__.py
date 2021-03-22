from flask import Flask 

from .commands import create_tables
from .extensions import db
from .models import DataModel

from .routes.savings import savings

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(savings)

    app.cli.add_command(create_tables)

    return app