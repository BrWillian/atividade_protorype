"""empty message

Revision ID: 88993162e8d9
Revises: aabbc805ec9d
Create Date: 2023-06-23 17:17:14.684203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88993162e8d9'
down_revision = 'aabbc805ec9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propriedade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cod_municipio', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'municipio', ['cod_municipio'], ['cod_municipio'])
        batch_op.drop_column('distancia_municipio')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propriedade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('distancia_municipio', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('cod_municipio')

    # ### end Alembic commands ###
