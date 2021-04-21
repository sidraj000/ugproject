from flask import Flask 

from .commands import create_tables
from .extensions import db
from .models import DataModel
from .routes.savings import savings
import os

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fddbhhljcdbkqu:169404ddc1e49eb071296be4315adac3ac680163d6386a778ca39e877b31cf85@ec2-52-0-114-209.compute-1.amazonaws.com:5432/d8hpdqra6gebcc"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:8529454669@localhost:5432/ugproject"
    # postgres://fddbhhljcdbkqu:169404ddc1e49eb071296be4315adac3ac680163d6386a778ca39e877b31cf85@ec2-52-0-114-209.compute-1.amazonaws.com:5432/d8hpdqra6gebcc
   
    db.init_app(app)

    app.register_blueprint(savings)

    app.cli.add_command(create_tables)
    @app.route('/',methods=['GET'])
    def hello():
         return {"msg":"working"}
    
    return app
    #device id- timestamp -data