from datetime import datetime, timedelta, timezone

from extensions import db
from flask import jsonify, request
from flask_restful import Resource
from models import Investments
from schemas import InvestmentsSchema, ProfitsSchema
from sqlalchemy import desc


class InvestmentsResource(Resource):
    @classmethod
    def get(cls):
        last_month = request.args.get("last_month")
        last_year = request.args.get("last_year")
        start_date_time = request.args.get("start_date_time")
        end_date_time = request.args.get("start_date_time")
        query = Investments.query

        if not any([last_month, last_year, start_date_time, end_date_time]):
            query = query

        elif last_month is not None:
            time = datetime.now(timezone.utc) - timedelta(days=30)
            query = query.filter(Investments.end_date_time > time)

        elif last_year is not None:
            time = datetime.now(timezone.utc) - timedelta(days=365)
            query = query.filter(Investments.end_date_time > time)

        elif start_date_time is not None and end_date_time is not None:
            start_date_time = datetime.strptime(
                start_date_time, "%Y-%m-%dT%H:%M:%S.%f%z"
            )
            end_date_time = datetime.strptime(end_date_time, "%Y-%m-%dT%H:%M:%S.%f%z")
            query = query.filter(
                Investments.end_date_time > start_date_time,
                Investments.end_date_time < end_date_time,
            )

        schema = InvestmentsSchema(many=True)
        investments = query.order_by(desc(Investments.start_date_time)).all()
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
