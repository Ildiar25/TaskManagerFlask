from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# This engine allows to connect SQLAlchemy with a database.
# Official documentation: https://docs.sqlalchemy.org/en/14/core/engines.html
engine = create_engine(
    "sqlite:///" +   # database language
    "database/tasks.db",  # database directory
    connect_args={"check_same_thread": False}  # Necessary with Flask
)

# Upper: According to documentation, the 'URL' attribute must contain the database language (sqlite on this case)
# and the main directory where database will be found. 'sqlite:///database/tasks.db' is the final result.
# 'check_same_thread' separate Flask from main process.

# WARNING: 'create_engine()' method does not connect directly to database, just defines its motor!

# Session allows interactions with the database.
Session = sessionmaker(bind=engine)
session = Session()

# Base class transform attributes to mapped data and link them to database table.
Base = declarative_base()
