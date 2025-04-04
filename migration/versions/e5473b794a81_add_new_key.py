"""add-new-key

Revision ID: e5473b794a81
Revises: 0a2b2ab80023
Create Date: 2025-03-29 19:23:13.880956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5473b794a81'
down_revision: Union[str, None] = '0a2b2ab80023'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('Profile', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'profile', ['Profile'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'Profile')
    # ### end Alembic commands ###
