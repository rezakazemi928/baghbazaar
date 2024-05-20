from extensions import db, ma
from marshmallow import fields
from models import Investments


class InvestmentsSchema(ma.SQLAlchemyAutoSchema):
    id = ma.UUID(dump_only=True)
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
        modle = Investments
        sqla_session = db.session
        load_instance = True
