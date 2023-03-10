"""uix_rate_currency_id_date

Revision ID: 7058801e0fe0
Revises: 6c89b7839f0c
Create Date: 2023-02-26 21:58:08.331331

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column, Integer, String, Boolean, update, text, delete, bindparam, select
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Inspector


# revision identifiers, used by Alembic.
revision = '7058801e0fe0'
down_revision = '6c89b7839f0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uix_rate_currency_id_date', 'rate', ['currency_id', 'date'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uix_rate_currency_id_date', 'rate', type_='unique')
    # ### end Alembic commands ###
