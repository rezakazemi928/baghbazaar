from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint(name="investment", url_prefix="/api")
api = Api(blueprint)
