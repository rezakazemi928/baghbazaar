from extensions import db, ma
from models import Profits


class ProfitsSchema(ma.SQLAlchemyAutoSchema):
    id = ma.UUID(dump_only=True)

    class Meta:
        model = Profits
        sqla_session = db.session
        load_instance = True
