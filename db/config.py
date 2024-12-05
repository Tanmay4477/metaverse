# from sqlmodel import SQLModel, create_engine, Session
# from models import *

# # Update the database URL for SQLite
# sqlite_db_url = 'sqlite:///sqlite.db'  # Using SQLite database file named 'sqlite.db'
# engine = create_engine(sqlite_db_url, echo=True)

# def start_db():
#     print("Server is running with SQLite instance")
#     SQLModel.metadata.create_all(engine)

# def get_session():
#     with Session(engine) as session:
#         print("Session started")
#         yield session


from sqlmodel import SQLModel, create_engine, Session
from models import *

postgres_db_url = 'postgresql+psycopg://db_username:db_password@localhost:5432/mydbmeta'
engine = create_engine(postgres_db_url, echo=True)

def start_db():
    print("Server is running with SQLite instance")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        print("Session started")
        yield session