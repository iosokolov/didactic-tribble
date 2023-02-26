"""uix_currency_code

Revision ID: 6c89b7839f0c
Revises: 47eda912d49f
Create Date: 2023-02-26 21:49:18.712239

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column, Integer, String, Boolean, update, text, delete, bindparam, select
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Inspector


# revision identifiers, used by Alembic.
revision = '6c89b7839f0c'
down_revision = '47eda912d49f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uix_currency_code', 'currency', ['code'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uix_currency_code', 'currency', type_='unique')
    # ### end Alembic commands ###
