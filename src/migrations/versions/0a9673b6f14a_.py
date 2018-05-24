"""empty message

Revision ID: 0a9673b6f14a
Revises: 55709530372f
Create Date: 2018-05-21 12:25:12.438216

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a9673b6f14a'
down_revision = '55709530372f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('component_license_conn')
    op.add_column('component', sa.Column('license_expression', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('component', 'license_expression')
    op.create_table('component_license_conn',
    sa.Column('component_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('license_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['component_id'], ['component.id'], name='component_license_conn_ibfk_1'),
    sa.ForeignKeyConstraint(['license_id'], ['license.id'], name='component_license_conn_ibfk_2'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
