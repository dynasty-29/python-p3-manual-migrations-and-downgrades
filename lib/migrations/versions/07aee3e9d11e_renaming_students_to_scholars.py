"""Renaming students to scholars

Revision ID: 07aee3e9d11e
Revises: 791279dd0760
Create Date: 2025-02-23 15:20:16.306374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07aee3e9d11e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
