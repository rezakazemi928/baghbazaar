"""empty message

Revision ID: b4651127214e
Revises: 
Create Date: 2024-05-20 15:00:39.846484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4651127214e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('investments',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('payment', sa.String(length=250), nullable=False),
    sa.Column('start_date_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('end_date_time', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('investments')
    # ### end Alembic commands ###