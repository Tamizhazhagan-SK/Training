import sys
import os

project_root = os.path.abspath(
os.path.join(os.path.dirname(__file__), "..", "..")
)

sys.path.insert(0, project_root)

from pyspark.sql import SparkSession
from modules.configurations.config import DatabaseConfig


def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("BMWCarsReader")
        .master("local[*]")
        .config(
            "spark.jars.packages",
            "org.postgresql:postgresql:42.7.1"
        )
        .getOrCreate()
    )

    return spark


def read_bmw_cars_table():
    spark = create_spark_session()

    df = (
        spark.read.format("jdbc")
        .option("url", DatabaseConfig.JDBC_URL)
        .option("dbtable", "bmw_cars")
        .option("user", DatabaseConfig.USER)
        .option("password", DatabaseConfig.PASSWORD)
        .option("driver", "org.postgresql.Driver")
        .load()
    )

    return df


if __name__ == "__main__":
    df = read_bmw_cars_table()

    print("BMW Cars Data:")
    df.show()

    print(f"Total Rows: {df.count()}")