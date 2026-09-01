import os
import sys
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, udf
from pyspark.sql.types import StringType

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CSV_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_customers.csv"

spark=SparkSession.builder \
    .appName("ETL Application") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "2g") \
    .config("spark.sql.shuffle.partitions", "4") \
    .master("local[*]") \
    .getOrCreate()

# Read the customer data from a CSV file into a DataFrame.
customer_df = spark.read.csv(str(CSV_PATH), header=True, inferSchema=True)

# Remove rows missing fields required for analysis.
required_columns = [
    "customer_id",
    "age",
    "model",
    "fuel_type",
    "city",
    "vehicle_year",
    "purchase_date",
    "purchase_price_inr",
    "annual_income_inr",
    "annual_km_driven",
    "satisfaction_score",
]
customer_df = customer_df.dropna(subset=required_columns)

# Parse purchase dates and keep vehicles purchased from 2023 through 2025.
customer_df = (
    customer_df
    .withColumn("purchase_date", to_date(col("purchase_date"), "yyyy-MM-dd"))
    .filter(
        col("purchase_date").between("2023-01-01", "2025-12-31")
    )
)

# Keep only valid values before converting monetary fields to integers.
customer_df = customer_df.filter(
    (col("age").between(18, 100))
    & (col("vehicle_year").between(1886, 2026))
    & (col("purchase_price_inr") > 0)
    & (col("annual_income_inr") > 0)
    & (col("annual_km_driven") >= 0)
    & (col("satisfaction_score").between(0, 5))
)

# Normalize numeric values for downstream analysis.
customer_df = (
    customer_df
    .withColumn("purchase_price_inr", col("purchase_price_inr").cast("int"))
    .withColumn("annual_income_inr", col("annual_income_inr").cast("int"))
    .withColumn("age", col("age").cast("int"))
    .withColumn("vehicle_year", col("vehicle_year").cast("int"))
    .withColumn("annual_km_driven", col("annual_km_driven").cast("int"))
)


# Classify vehicles by purchase price in Indian rupees.
def classify_price(purchase_price_inr):
    if purchase_price_inr <= 7000000:
        return "Budget"
    elif purchase_price_inr <= 15000000:
        return "Premium"
    else:
        return "Luxury"


classify_price_udf = udf(classify_price, StringType())

customer_df = customer_df.withColumn(
    "price_category",
    classify_price_udf(col("purchase_price_inr")),
)

# Store the cleaned customer data as a Parquet report.
REPORTS_DIR = PROJECT_ROOT / "src" / "modules" / "reports"
PARQUET_PATH = REPORTS_DIR / "bmw_customers.parquet"

customer_df.write.mode("overwrite").parquet(str(PARQUET_PATH))

spark_ui_url = spark.sparkContext.uiWebUrl or "unavailable"
print(f"ETL completed successfully. Parquet file saved to: {PARQUET_PATH}")
print(f"Spark UI: {spark_ui_url}")
spark.stop()