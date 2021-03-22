from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)
    #for production
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # for local
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:8529454669@localhost:5432/ugproject"
    
    db.init_app(app)
    migrate = Migrate(app, db)
    from app import models


    from .savings import savings as savings_blueprint
    app.register_blueprint(savings_blueprint)
    db.create_all()
 

    @app.route('/health', methods=['GET'])
    def hello_world():
     return {'project': 'running '}

    return app
