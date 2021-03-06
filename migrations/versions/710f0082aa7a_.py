"""empty message

Revision ID: 710f0082aa7a
Revises: 
Create Date: 2020-01-06 21:45:27.127868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '710f0082aa7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grocery_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('checked', sa.Boolean(), nullable=False),
    sa.Column('dollars', sa.Integer(), nullable=False),
    sa.Column('cents', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hash', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('grocery_item')
    # ### end Alembic commands ###
