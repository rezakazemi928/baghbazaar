from extensions import db
from flask import jsonify, request
from flask_restful import Resource
from models import Investments
from schemas import InvestmentsSchema, ProfitsSchema


class InvestmentsResource(Resource):
    @classmethod
    def get(cls):
        schema = InvestmentsSchema(many=True)
        investments = Investments.query.all()
        return jsonify(schema.dump(investments))

    @classmethod
    def post(cls):
        req_obj = request.json
        schema = InvestmentsSchema(partial=True)
        investment = schema.load(req_obj)
        db.session.add(investment)
        db.session.commit()
        return jsonify(schema.dump(investment))


class ProfitsResource(Resource):
    @classmethod
    def post(cls):
        req_obj = request.json
        schema = ProfitsSchema()
        profit = schema.load(req_obj)
        db.session.add(profit)
        db.session.commit()
        return jsonify(schema.dump(profit))
