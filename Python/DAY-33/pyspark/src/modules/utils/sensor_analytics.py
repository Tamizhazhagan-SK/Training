import os
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, round, to_timestamp


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SENSOR_DATA_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_sensor_raw_data.txt"
ORIGINAL_REPORT_PATH = PROJECT_ROOT / "src" / "modules" / "reports" / "bmw_sensor_original.parquet"
REPORT_PATH = PROJECT_ROOT / "src" / "modules" / "reports" / "bmw_sensor_data.parquet"


spark = (
    SparkSession.builder
    .appName("BMW Sensor Analytics")
    .config("spark.sql.shuffle.partitions", "4")
    .master("local[*]")
    .getOrCreate()
)

try:
    sensor_df = (
        spark.read
        .option("header", True)
        .option("delimiter", "#")
        .option("inferSchema", True)
        .csv(str(SENSOR_DATA_PATH))
    )

    cleaned_sensor_df = (
        sensor_df
        .withColumn("timestamp", to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss"))
        .withColumn("engine_rpm", col("engine_rpm").cast("double"))
        .withColumn("engine_temp_c", col("engine_temp_c").cast("double"))
        .withColumn("oil_temp_c", col("oil_temp_c").cast("double"))
        .dropna(subset=["vehicle_id", "engine_rpm", "engine_temp_c", "oil_temp_c"])
    )

    sensor_df.write.mode("overwrite").parquet(str(ORIGINAL_REPORT_PATH))

    drive_mode_averages_df = (
        cleaned_sensor_df.groupBy("drive_mode")
        .agg(
            round(avg("engine_rpm"), 2).alias("average_engine_rpm"),
            round(avg("engine_temp_c"), 2).alias("average_engine_temp_c"),
            round(avg("oil_temp_c"), 2).alias("average_oil_temp_c"),
        )
        .orderBy("drive_mode")
    )

    drive_mode_averages_df.write.mode("overwrite").parquet(str(REPORT_PATH))

    print(f"Sensor records processed: {cleaned_sensor_df.count()}")
    print(f"Original sensor records saved to: {ORIGINAL_REPORT_PATH}")
    print("Average sensor values by drive mode:")
    drive_mode_averages_df.show(truncate=False)
    print(f"Averages Parquet report saved to: {REPORT_PATH}")
finally:
    spark.stop()
