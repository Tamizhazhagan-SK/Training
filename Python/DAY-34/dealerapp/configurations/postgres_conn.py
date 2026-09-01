import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Example Postgres URL:
#   postgresql+psycopg2://<user>:<password>@<host>:<port>/<database>
# Falls back to a local SQLite file if DATABASE_URL isn't set, so the app
# can be exercised without a running Postgres instance (e.g. for quick
# local testing). Set DATABASE_URL to point at real Postgres for the
# intended exercise.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/bmw_dealer_inventory",
)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """FastAPI dependency that yields a DB session and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Create all tables. Call once at application startup."""
    # Import models here so they're registered on Base before create_all.
    from models import dealer, vehicle  # noqa: F401

    Base.metadata.create_all(bind=engine)
