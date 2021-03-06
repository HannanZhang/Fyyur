"""empty message

Revision ID: 8758db340fc4
Revises: ae7349cf1495
Create Date: 2021-10-29 20:06:20.317443

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8758db340fc4'
down_revision = 'ae7349cf1495'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('start_time', sa.DateTime(), nullable=False))
    op.drop_column('shows', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('shows', 'start_time')
    # ### end Alembic commands ###
