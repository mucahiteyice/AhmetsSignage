"""empty message

Revision ID: ccaaca3fc327
Revises: c2b4a01928ad
Create Date: 2020-02-13 22:18:57.595065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccaaca3fc327'
down_revision = 'c2b4a01928ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('yemekler1', sa.Column('yemekicerik', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('yemekler1', 'yemekicerik')
    # ### end Alembic commands ###
