"""Initial migration.

Revision ID: c9558e0038c5
Revises: 
Create Date: 2023-12-11 21:01:19.974457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9558e0038c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=200), nullable=False),
    sa.Column('company_logo', sa.LargeBinary(), nullable=True),
    sa.Column('desc', sa.String(length=500), nullable=False),
    sa.Column('industry', sa.String(length=250), nullable=False),
    sa.Column('campus_cp', sa.String(length=300), nullable=False),
    sa.Column('website_url', sa.String(length=500), nullable=True),
    sa.Column('email_cp', sa.String(length=120), nullable=False),
    sa.Column('company_size_min', sa.Integer(), nullable=True),
    sa.Column('company_size_max', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_cp')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.Column('profile_image', sa.LargeBinary(), nullable=True),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('email_st', sa.String(length=120), nullable=False),
    sa.Column('dept', sa.String(length=80), nullable=False),
    sa.Column('skills', sa.String(length=300), nullable=True),
    sa.Column('campus_st', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_st'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('company')
    # ### end Alembic commands ###
