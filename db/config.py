from sqlmodel import SQLModel, create_engine, Session
from models import *

# local_postgres_db_url = 'postgresql+psycopg://db_username:db_password@localhost:5432/mydbmeta'
postgres_db_url = 'postgresql+psycopg://postgres:mysecretpassword@3.110.48.240:5432/postgres'
engine = create_engine(postgres_db_url, echo=True)

def start_db():
    print("Server is running with Postgres instance")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        print("Session started")
        yield session