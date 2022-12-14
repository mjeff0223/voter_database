"""empty message

Revision ID: d1abaae0712c
Revises: d4e6ee0d4ab0
Create Date: 2022-09-01 22:09:05.747353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1abaae0712c'
down_revision = 'd4e6ee0d4ab0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidates',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('candidate_name', sa.String(length=128), nullable=False),
    sa.Column('party', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voters',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('party_affiliation', sa.String(length=128), nullable=False),
    sa.Column('voter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['voter_id'], ['voters.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('ballots',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('voter_id', sa.Integer(), nullable=False),
    sa.Column('voted_for', sa.String(length=128), nullable=False),
    sa.Column('voted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['voter_id'], ['voters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('districts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('state', sa.String(length=128), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['voter_id'], ['voters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pacs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('issue', sa.String(length=128), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['voter_id'], ['voters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pacs_voters',
    sa.Column('voter_id', sa.Integer(), nullable=False),
    sa.Column('pac_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pac_id'], ['pacs.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['voters.id'], ),
    sa.PrimaryKeyConstraint('voter_id', 'pac_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pacs_voters')
    op.drop_table('pacs')
    op.drop_table('districts')
    op.drop_table('ballots')
    op.drop_table('accounts')
    op.drop_table('voters')
    op.drop_table('candidates')
    # ### end Alembic commands ###
