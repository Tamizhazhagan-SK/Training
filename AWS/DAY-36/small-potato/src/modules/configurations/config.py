import os
from dotenv import load_dotenv

load_dotenv()


class DatabaseConfig:
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    DATABASE = os.getenv("DB_NAME")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")

    JDBC_URL = (
        f"jdbc:postgresql://{HOST}:{PORT}/{DATABASE}"
    )