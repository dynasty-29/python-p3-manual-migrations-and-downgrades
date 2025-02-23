"""Renaming birthday to dob

Revision ID: 7afc8304501c
Revises: 07aee3e9d11e
Create Date: 2025-02-23 15:27:17.280478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7afc8304501c'
down_revision = '07aee3e9d11e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'birthday', new_column_name='dob')


def downgrade() -> None:
    op.alter_column('students', 'dob', new_column_name='birthday')
