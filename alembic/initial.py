from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('amount', sa.Integer, nullable=False),
        sa.Column('type', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('timestamp', sa.DateTime, server_default=sa.text('(now() at time zone \'utc\')'))
    )

def downgrade():
    op.drop_table('transactions')
