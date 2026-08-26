from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from modules.configurations.config import Config




config = Config().get_database_connection_string().replace(
    "postgresql+psycopg2://", "postgresql+psycopg://"
)

base = declarative_base()

engine = create_async_engine(
    config,
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)

sessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class PGConnection:
    @staticmethod
    async def get_connection():
        return await engine.connect()

    @staticmethod
    def get_session():
        return sessionLocal()
    
    @staticmethod
    async def close_connection(conn):
        await conn.close()




