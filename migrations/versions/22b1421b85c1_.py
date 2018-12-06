"""empty message

Revision ID: 22b1421b85c1
Revises: ed579e5b057e
Create Date: 2018-11-18 16:54:07.445225

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '22b1421b85c1'
down_revision = 'ed579e5b057e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Project',
    sa.Column('projectNo', sa.Integer(), nullable=False),
    sa.Column('projectName', sa.String(length=30), nullable=True),
    sa.Column('projectMan', sa.String(length=10), nullable=True),
    sa.Column('howmany', sa.Integer(), nullable=True),
    sa.Column('time', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('projectNo'),
    sa.UniqueConstraint('projectName')
    )
    op.drop_index('projectName', table_name='project')
    op.drop_table('project')
    op.add_column('ProjectEssay', sa.Column('pro_author', sa.String(length=4), nullable=True))
    op.add_column('ProjectEssay', sa.Column('pro_content', sa.Text(), nullable=True))
    op.add_column('ProjectEssay', sa.Column('pro_title', sa.String(length=10), nullable=True))
    op.add_column('ProjectEssay', sa.Column('pro_type', sa.String(length=10), nullable=True))
    op.add_column('ProjectEssay', sa.Column('pro_updateTime', sa.Date(), nullable=True))
    op.add_column('ProjectEssay', sa.Column('projectNo', sa.Integer(), nullable=True))
    op.drop_constraint('ProjectEssay_ibfk_1', 'ProjectEssay', type_='foreignkey')
    op.create_foreign_key(None, 'ProjectEssay', 'Project', ['projectNo'], ['projectNo'])
    op.drop_column('ProjectEssay', 'essayNo')
    op.drop_column('ProjectEssay', 'pro_design')
    op.add_column('hubuser', sa.Column('logintime', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hubuser', 'logintime')
    op.add_column('ProjectEssay', sa.Column('pro_design', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('ProjectEssay', sa.Column('essayNo', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'ProjectEssay', type_='foreignkey')
    op.create_foreign_key('ProjectEssay_ibfk_1', 'ProjectEssay', 'Essay', ['essayNo'], ['essayNo'])
    op.drop_column('ProjectEssay', 'projectNo')
    op.drop_column('ProjectEssay', 'pro_updateTime')
    op.drop_column('ProjectEssay', 'pro_type')
    op.drop_column('ProjectEssay', 'pro_title')
    op.drop_column('ProjectEssay', 'pro_content')
    op.drop_column('ProjectEssay', 'pro_author')
    op.create_table('project',
    sa.Column('projectNo', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('projectName', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('howmany', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('projectMan', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('time', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('projectNo'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('projectName', 'project', ['projectName'], unique=True)
    op.drop_table('Project')
    # ### end Alembic commands ###
