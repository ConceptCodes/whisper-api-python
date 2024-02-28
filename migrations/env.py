from logging.config import fileConfig

from alembic import context

from sqlmodel import SQLModel                   # New

config = context.config
fileConfig(config.config_file_name)

# Model / Schema imports
from core.models.db import Users, Transcripts, Uploads, Queue  # Updated

target_metadata = SQLModel.metadata             # Updated

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()
        