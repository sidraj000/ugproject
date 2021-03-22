from flask import Flask 

from .commands import create_tables
from .extensions import db
from .models import DataModel

from .routes.savings import savings
import os

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:8529454669@localhost:5432/ugproject"
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    print(os.environ['DATABASE_URL'])
    db.init_app(app)

    app.register_blueprint(savings)

    app.cli.add_command(create_tables)
    @app.route('/',methods=['GET'])
    def hello():
         return {"msg":"working"}
    
    return app