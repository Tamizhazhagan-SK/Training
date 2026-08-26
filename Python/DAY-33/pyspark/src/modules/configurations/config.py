import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / "src" / "modules" / ".env")


def _setting(name: str, legacy_name: str, default: str) -> str:
    return os.getenv(name, os.getenv(legacy_name, default))


class Config:
    def __init__(self):
        self.postgres_host = _setting("POSTGRES_HOST", "host", "localhost")
        self.postgres_port = _setting("POSTGRES_PORT", "port", "5432")
        self.postgres_database = _setting("POSTGRES_DB", "pg_database", "bmwdb")
        self.postgres_user = _setting("POSTGRES_USER", "pg_user", "postgres")
        self.vehicle_table = _setting("VEHICLE_TABLE", "vehicle_table", "vehicle")
        self.postgres_password = _setting(
            "POSTGRES_PASSWORD", "pg_password", "postgres"
        )

    @property
    def jdbc_url(self) -> str:
        return (
            f"jdbc:postgresql://{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_database}"
        )

    @property
    def jdbc_properties(self) -> dict[str, str]:
        return {
            "user": self.postgres_user,
            "password": self.postgres_password,
            "driver": "org.postgresql.Driver",
        }

    def get_database_connection_string(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_database}"
        )

    def get_jdbc_connection_string(self) -> str:
        return self.jdbc_url

