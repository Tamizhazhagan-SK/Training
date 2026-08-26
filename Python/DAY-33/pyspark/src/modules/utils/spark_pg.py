from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

from modules.configurations.config import Config


def get_spark_session() -> SparkSession:
    return (
        SparkSession.builder
        .appName("BMW PostgreSQL ETL")
        .config("spark.jars.packages", "org.postgresql:postgresql:42.7.5")
        .master("local[*]")
        .getOrCreate()
    )


def read_postgres_table(
    spark: SparkSession,
    table_name: str,
    config: Config | None = None,
) -> DataFrame:
    database_config = config or Config()
    return (
        spark.read
        .format("jdbc")
        .option("url", database_config.get_jdbc_connection_string())
        .option("dbtable", table_name)
        .options(**database_config.jdbc_properties)
        .load()
    )


if __name__ == "__main__":
    config = Config()
    spark = get_spark_session()
    try:
        vehicles = read_postgres_table(spark, config.vehicle_table, config)
        vehicles.show()
    finally:
        spark.stop()

         