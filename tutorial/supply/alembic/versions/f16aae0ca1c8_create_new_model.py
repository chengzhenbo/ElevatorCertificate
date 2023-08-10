"""create new model

Revision ID: f16aae0ca1c8
Revises: 9979853d2e45
Create Date: 2023-08-10 14:21:50.168145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f16aae0ca1c8'
down_revision = '9979853d2e45'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier_safe_brake', sa.Column('user_id', sa.BigInteger(), nullable=True, comment='操作用户ID'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplier_safe_brake', 'user_id')
    # ### end Alembic commands ###
