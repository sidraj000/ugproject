from flask import Blueprint

savings = Blueprint('savings', __name__)

from . import views