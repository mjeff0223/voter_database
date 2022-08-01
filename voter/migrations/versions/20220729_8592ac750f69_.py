"""empty message

Revision ID: 8592ac750f69
Revises: 74ee2acbfb33
Create Date: 2022-07-29 13:42:40.178852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8592ac750f69'
down_revision = '74ee2acbfb33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pacs', 'money_raised')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pacs', sa.Column('money_raised', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
