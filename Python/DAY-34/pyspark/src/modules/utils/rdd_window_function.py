from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import (
    avg,
    col,
    dense_rank,
    rank,
    row_number,
    round as spark_round,
)

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CSV_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_customers.csv"

spark = (
    SparkSession.builder
    .appName("BMW Customer Window Functions")
    .config("spark.sql.shuffle.partitions", "4")
    .master("local[*]")
    .getOrCreate()
)

customer_df = spark.read.csv(str(CSV_PATH), header=True, inferSchema=True)

# --- Window spec: partition by city, order by purchase price descending ---
city_price_window = Window.partitionBy("city").orderBy(col("purchase_price_inr").desc())

customer_df = (
    customer_df
    .withColumn("row_number_in_city", row_number().over(city_price_window))
    .withColumn("rank_in_city", rank().over(city_price_window))
    .withColumn("dense_rank_in_city", dense_rank().over(city_price_window))
)

print("Top spender per city (row_number = 1):")
(customer_df
 .filter(col("row_number_in_city") == 1)
 .select("city", "customer_id", "purchase_price_inr", "rank_in_city")
 .orderBy("city")
 .show(20, truncate=False))

# --- Window spec: partition by model, no ordering needed for an aggregate ---
model_window = Window.partitionBy("model")

customer_df = customer_df.withColumn(
    "avg_income_by_model",
    spark_round(avg("annual_income_inr").over(model_window), 2),
)

print("Sample rows showing per-model average income alongside individual income:")
(customer_df
 .select("customer_id", "model", "annual_income_inr", "avg_income_by_model")
 .orderBy("model")
 .show(10, truncate=False))

spark.stop()