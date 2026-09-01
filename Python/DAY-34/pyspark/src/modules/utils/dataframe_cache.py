import time

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count

HDFS_CSV_PATH = "hdfs://namenode:9000/data/bmw_customers.csv"

spark = (
    SparkSession.builder
    .appName("BMW Customer DataFrame Caching")
    .config("spark.sql.shuffle.partitions", "4")
    .master("spark://spark-master:7077")
    .getOrCreate()
)

customer_df = spark.read.csv(HDFS_CSV_PATH, header=True, inferSchema=True)

# --- WITHOUT caching: every action re-reads the CSV and re-runs the plan ---
start = time.time()
print(f"Uncached count: {customer_df.count()}")
print(f"Uncached avg income: {customer_df.agg(avg('annual_income_inr')).collect()[0][0]:.2f}")
print(f"Uncached state group count: {customer_df.groupBy('state').agg(count('*')).count()}")
print(f"Time without caching: {time.time() - start:.3f}s\n")

# --- WITH caching: materialize once, reuse across actions ---
customer_df.cache()

start = time.time()
# The FIRST action after .cache() still does the full read + computation --
# that's what actually populates the cache. Caching is lazy, just like
# transformations, until an action forces it to run.
print(f"Cached count (first action, populates cache): {customer_df.count()}")
print(f"Cached avg income: {customer_df.agg(avg('annual_income_inr')).collect()[0][0]:.2f}")
print(f"Cached state group count: {customer_df.groupBy('state').agg(count('*')).count()}")
print(f"Time with caching: {time.time() - start:.3f}s")

# Confirm it's actually cached
print(f"\nIs cached: {customer_df.storageLevel.useMemory}")

customer_df.unpersist()
spark.stop()