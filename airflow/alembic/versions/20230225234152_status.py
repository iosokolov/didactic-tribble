"""status

Revision ID: 20a03a9a35c3
Revises: 3dc3396ddf40
Create Date: 2023-02-25 23:41:52.356882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column, Integer, String, Boolean, update, text, delete, bindparam, select
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Inspector


# revision identifiers, used by Alembic.
revision = '20a03a9a35c3'
down_revision = '3dc3396ddf40'
branch_labels = None
depends_on = None


status_enum = postgresql.ENUM(
    "PENDING",
    "COMPLETED",
    "ERROR",
    "RESERVED_FOR_FUTURE_USE_1",
    "RESERVED_FOR_FUTURE_USE_2",
    "RESERVED_FOR_FUTURE_USE_3",
    "RESERVED_FOR_FUTURE_USE_4",
    "RESERVED_FOR_FUTURE_USE_5",
    "RESERVED_FOR_FUTURE_USE_6",
    "RESERVED_FOR_FUTURE_USE_7",
    "RESERVED_FOR_FUTURE_USE_8",
    "RESERVED_FOR_FUTURE_USE_9",
    "RESERVED_FOR_FUTURE_USE_10",
    name="status_enum",
    create_type=False,
)


def upgrade() -> None:
    status_enum.create(op.get_bind())
    op.add_column('record', sa.Column('request_uuid', sa.UUID(), nullable=False))
    op.add_column('record', sa.Column('status', status_enum, nullable=False))
    op.create_index(op.f('ix_record_request_uuid'), 'record', ['request_uuid'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_record_request_uuid'), table_name='record')
    op.drop_column('record', 'status')
    op.drop_column('record', 'request_uuid')
    status_enum.drop(op.get_bind())
