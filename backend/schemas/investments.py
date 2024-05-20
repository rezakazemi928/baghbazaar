from datetime import datetime, timedelta, timezone

from extensions import db, ma
from marshmallow import fields, post_dump, pre_load
from models import Investments


class InvestmentsSchemaBase(ma.SQLAlchemyAutoSchema):
    end_in = ma.Integer(load_only=True, required=True)
    profits = fields.List(
        fields.Nested(
            "ProfitsSchema",
            only=(
                "id",
                "amount",
                "date_time",
            ),
        ),
        allow_none=True,
        required=False,
    )

    class Meta:
        model = Investments
        sqla_session = db.session
        load_instance = True


class InvestmentsSchema(InvestmentsSchemaBase):
    id = ma.UUID(dump_only=True)

    class Meta:
        model = Investments
        sqla_session = db.session
        load_instance = True

    @pre_load
    def prepare_req_data(self, data, **kwargs):
        data["end_date_time"] = (
            datetime.now(timezone.utc) + timedelta(seconds=int(data["end_in"]))
        ).strftime("%Y-%m-%dT%H:%M:%S")
        # del data["end_in"]

        return data

    @post_dump
    def prepare_response(self, response, **kwargs):
        total = int(response["payment"])
        total_profit = 0
        if response["profits"] is not None and len(response["profits"]) != 0:
            for profit in response["profits"]:
                total = total + int(profit["amount"])
                total_profit = total_profit + int(profit["amount"])

        response["total"] = total
        response["total_profit"] = total_profit
        return response
