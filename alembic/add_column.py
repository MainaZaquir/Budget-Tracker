from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('transactions', sa.Column('new_column', sa.String))

def downgrade():
    op.drop_column('transactions', 'new_column')
