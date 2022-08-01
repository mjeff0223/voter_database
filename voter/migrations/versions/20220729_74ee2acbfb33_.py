"""empty message

Revision ID: 74ee2acbfb33
Revises: 06f5bab16ecf
Create Date: 2022-07-29 13:40:27.162672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74ee2acbfb33'
down_revision = '06f5bab16ecf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'accounts', 'voters', ['voter_id'], ['id'])
    op.alter_column('pacs', 'issue',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('pacs', 'voter_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_constraint('pacs_name_key', 'pacs', type_='unique')
    op.create_foreign_key(None, 'pacs_voters', 'pacs', ['pac_id'], ['id'])
    op.create_foreign_key(None, 'pacs_voters', 'voters', ['voter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pacs_voters', type_='foreignkey')
    op.drop_constraint(None, 'pacs_voters', type_='foreignkey')
    op.create_unique_constraint('pacs_name_key', 'pacs', ['name'])
    op.alter_column('pacs', 'voter_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.alter_column('pacs', 'issue',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_constraint(None, 'accounts', type_='foreignkey')
    # ### end Alembic commands ###
