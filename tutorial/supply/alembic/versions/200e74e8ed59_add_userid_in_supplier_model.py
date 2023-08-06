"""add userid in supplier model

Revision ID: 200e74e8ed59
Revises: 3fa7ad51ca56
Create Date: 2023-08-06 21:15:13.279542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '200e74e8ed59'
down_revision = '3fa7ad51ca56'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier_smart_board', sa.Column('user_id', sa.BigInteger(), nullable=True, comment='操作用户id'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplier_smart_board', 'user_id')
    # ### end Alembic commands ###
