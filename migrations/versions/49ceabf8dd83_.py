"""empty message

Revision ID: 49ceabf8dd83
Revises: 775780a8ceee
Create Date: 2016-03-26 13:29:26.633614

"""

# revision identifiers, used by Alembic.
revision = '49ceabf8dd83'
down_revision = '775780a8ceee'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wishlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.String(length=15), nullable=True),
    sa.Column('modified_at', sa.String(length=15), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('wishlist_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['wishlist_id'], ['wishlist.id'], )
    )
    op.add_column(u'item', sa.Column('thumbnail', sa.String(length=500), nullable=True))
    op.add_column(u'item', sa.Column('wishlist_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'user', ['wishlist_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column(u'item', 'wishlist_id')
    op.drop_column(u'item', 'thumbnail')
    op.drop_table('items')
    op.drop_table('wishlist')
    ### end Alembic commands ###
