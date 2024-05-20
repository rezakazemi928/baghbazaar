from apis.resources import InvestmentsResource
from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint("investment", __name__, url_prefix="/api")
api = Api(blueprint)


api.add_resource(InvestmentsResource, "/investments", endpoint="investments")
