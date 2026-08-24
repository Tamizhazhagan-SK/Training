from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from modules.configurations.config import Config




config = Config.get_database_connection_string()

base = declarative_base()

engine = create_engine(config, echo=True, pool_size=10, max_overflow=20, pool_timeout=30, pool_recycle=1800, pool_pre_ping=True)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class PGConnection:
    @staticmethod
    def get_connection():
        return engine.connect()

    @staticmethod
    def get_session():
        return sessionLocal()
    
    @staticmethod
    def close_connection(conn):
        conn.close()




