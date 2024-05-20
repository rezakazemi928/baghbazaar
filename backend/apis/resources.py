from extensions import db
from flask import jsonify, request
from flask_restful import Resource
from schemas import InvestmentsSchema


class InvestmentsResource(Resource):
    @classmethod
    def get(cls):
        pass

    @classmethod
    def post(cls):
        req_obj = request.json
        schema = InvestmentsSchema(partial=True)
        investment = schema.load(req_obj)
        db.session.add(investment)
        db.session.commit()
        return jsonify(schema.dump(investment))
