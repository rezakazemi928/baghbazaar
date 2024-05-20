import uuid

from extensions import db
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID


class Investments(db.Model):
    __tablename__ = "investments"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = db.Column(db.String(40), nullable=False, unique=True)
    payment = db.Column(db.String(250), nullable=False)
    start_date_time = db.Column(
        db.DateTime(timezone=True), nullable=False, default=func.now()
    )
    end_date_time = db.Column(db.DateTime(timezone=True), nullable=False)
    profits = db.relationship("Profits", backref="profits", lazy=True)
