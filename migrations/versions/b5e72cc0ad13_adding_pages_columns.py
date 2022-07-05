"""adding_pages_columns

Revision ID: b5e72cc0ad13
Revises: 20f6e3c56986
Create Date: 2022-07-05 17:03:53.536096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5e72cc0ad13'
down_revision = '20f6e3c56986'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('pages', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'pages')
    # ### end Alembic commands ###


