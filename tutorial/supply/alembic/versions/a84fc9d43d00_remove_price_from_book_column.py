"""remove price from book column

Revision ID: a84fc9d43d00
Revises: bf14f7aae2ee
Create Date: 2023-08-04 15:47:59.847705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a84fc9d43d00'
down_revision = 'bf14f7aae2ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'price')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('price', sa.FLOAT(), nullable=True))
    # ### end Alembic commands ###
