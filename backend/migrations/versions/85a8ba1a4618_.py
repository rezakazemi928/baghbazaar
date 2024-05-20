"""empty message

Revision ID: 85a8ba1a4618
Revises: b4651127214e
Create Date: 2024-05-20 15:51:04.213177

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "85a8ba1a4618"
down_revision = "b4651127214e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "investments", ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "investments", type_="unique")
    # ### end Alembic commands ###
