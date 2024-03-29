"""05_Add_sign_of_booking_by_administrator

Revision ID: 9f9ddd314157
Revises: 380592f49f55
Create Date: 2024-02-04 19:20:16.380912

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '9f9ddd314157'
down_revision: Union[str, None] = '380592f49f55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('azucafe_order', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('admin_booking', sa.Boolean(), nullable=True)
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('azucafe_order', schema=None) as batch_op:
        batch_op.drop_column('admin_booking')

        # ### end Alembic commands ###
