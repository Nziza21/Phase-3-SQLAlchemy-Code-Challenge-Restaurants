from alembic import context
from app import create_app, db 

app = create_app()
app.app_context().push()

connection = app.extensions['sqlalchemy'].db.engine.connect()
context.configure(connection=connection, target_metadata=db.metadata)