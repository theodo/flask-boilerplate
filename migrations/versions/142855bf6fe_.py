"""empty message

Revision ID: 142855bf6fe
Revises: None
Create Date: 2015-02-27 14:27:47.365509

"""

# revision identifiers, used by Alembic.
revision = '142855bf6fe'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('auth_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('auth_user')
