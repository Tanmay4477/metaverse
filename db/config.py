from sqlmodel import SQLModel, create_engine, Session
from models import *

postgres_db_url = 'postgresql://postgres:tanmay@localhost:5432/postgres'
engine = create_engine(postgres_db_url, echo=True)

def start_db():
    print("Server is running on local instance")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        print("Session started")
        yield session
    






