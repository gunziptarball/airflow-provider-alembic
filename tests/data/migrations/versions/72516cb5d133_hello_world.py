"""Example of a migration
Revision ID: 72516cb5d133
Revises: 
Create Date: 2021-09-20 00:43:04.258358

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "72516cb5d133"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("foobar", sa.Column("id", sa.Integer, primary_key=True))


def downgrade():
    op.drop_table("foobar")
