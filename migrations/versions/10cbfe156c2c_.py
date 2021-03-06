"""empty message

Revision ID: 10cbfe156c2c
Revises: ae538bc531d1
Create Date: 2016-03-26 19:40:46.297043

"""

# revision identifiers, used by Alembic.
revision = '10cbfe156c2c'
down_revision = 'ae538bc531d1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('expire_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.add_column(u'user', sa.Column('last_login_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user', 'last_login_at')
    op.drop_table('auth_token')
    ### end Alembic commands ###
