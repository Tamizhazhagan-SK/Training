import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

PROJECT_ROOT = Path(__file__).resolve().parents[3]
CSV_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_customers.csv"

spark = (
    SparkSession.builder
    .appName("BMW Customer State Broadcast")
    .config("spark.sql.shuffle.partitions", "4")
    .master("local[*]")
    .getOrCreate()
)

customer_df = spark.read.csv(str(CSV_PATH), header=True, inferSchema=True)

# Small, static lookup table -- a perfect candidate for broadcasting
state_short_codes = {
    "Tamil Nadu": "TN",
    "Kerala": "KL",
    "Karnataka": "KA",
    "Telangana": "TS",
    "Maharashtra": "MH",
    "Haryana": "HR",
    "Rajasthan": "RJ",
    "Gujarat": "GJ",
    "Uttar Pradesh": "UP",
    "Bihar": "BR",
    "Delhi": "DL",
    "West Bengal": "WB",
    "Chandigarh": "CH",
    "Andhra Pradesh": "AP"
}

# Broadcast it once -- every executor gets its own cached copy,
# instead of Spark re-shipping the dict with every single task
state_codes_bc = spark.sparkContext.broadcast(state_short_codes)
    

def lookup_state_code(state_name):
    """Look up the broadcasted mapping to get a state's short code."""
    return state_codes_bc.value.get(state_name, "NA")


lookup_state_code_udf = udf(lookup_state_code, StringType())

customer_df = customer_df.withColumn(
    "state_code",
    lookup_state_code_udf(col("state")),
)

print(f"Total records: {customer_df.count()}")
customer_df.select("customer_id", "state", "state_code").show(10, truncate=False)

spark.stop()