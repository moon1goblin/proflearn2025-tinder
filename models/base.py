from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import get_settings

Settings = get_settings()

# db dsm
engine = create_engine("postgresql://postgres:@localhost:5432")
db_session = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    with db_session() as session:
        yield session
