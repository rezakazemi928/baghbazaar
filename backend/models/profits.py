import uuid

from extensions import db
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID


class Profits(db.Model):
    __tablename__ = "profits"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        unique=True,
        default=uuid.uuid4,
    )
    amount = db.Column(db.String(40), nullable=False)
    investment_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("investments.id", ondelete="CASCADE"),
        nullable=False,
        unique=False,
    )
    date_time = db.Column(
        db.DateTime(timezone=True), nullable=False, default=func.now()
    )
