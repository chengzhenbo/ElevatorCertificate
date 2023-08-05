"""add new column for book

Revision ID: 7618d6f7c1e4
Revises: 47ac1a3fdbdf
Create Date: 2023-08-04 15:22:23.316040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7618d6f7c1e4'
down_revision = '47ac1a3fdbdf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'price')
    # ### end Alembic commands ###