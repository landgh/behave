from src_py.database import connect_db, close_db

def before_all(context):
    # Initialize database connection
    context.db_connection = connect_db()

def after_all(context):
    # Close database connection
    close_db(context.db_connection)
