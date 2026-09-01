"""
BMW Customers — RDD Analysis (S3 -> local Parquet)
====================================================

Reads bmw_customers.csv from S3 (s3://small-potato/friday/bmw_customers.csv),
does the actual analysis using RDD transformations (map / filter /
reduceByKey), then writes each result as a local Parquet file under
the reports/ folder inside this project.

Prerequisites
-------------
1. Hadoop + PySpark already configured (per your setup). Your PySpark
   install bundles Hadoop client 3.5.0, so hadoop-aws must be 3.5.0 too
   (Hadoop 3.4+ switched hadoop-aws to AWS SDK v2 — mixing an older
   hadoop-aws with a newer Hadoop client is what caused the earlier
   NumberFormatException: For input string: "60s").

2. No need for spark-submit or --packages — this script pulls the S3A
   jars itself via spark.jars.packages. Just run:

       python rdd.py

3. AWS credentials: this script reads them from the same environment
   variables your boto3 upload script already relies on
   (AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / optionally
   AWS_SESSION_TOKEN). Set them in PowerShell before running if they
   aren't already in your environment:

       $env:AWS_ACCESS_KEY_ID = "..."
       $env:AWS_SECRET_ACCESS_KEY = "..."
"""

import os
import sys
import glob
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, DoubleType
)

# Pin the driver + worker interpreter explicitly to whatever Python is
# currently running this script. Without this, Spark on Windows can
# sometimes try to re-derive the interpreter path itself and fail to
# spawn worker subprocesses with:
#   "Cannot run program '...\\.venv\\Scripts\\python.exe': CreateProcess
#    error=2, The system cannot find the file specified"
# This is especially common when the venv lives inside a OneDrive-synced
# folder, where python.exe can end up as an unhydrated cloud placeholder.
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# Hadoop's local-filesystem code needs winutils.exe / hadoop.dll on
# Windows for native file-permission checks — without this you get:
#   UnsatisfiedLinkError: 'boolean NativeIO$Windows.access0(...)'
# Download both files from https://github.com/cdarlint/winutils
# (hadoop-3.3.6/bin folder) into the path below, and also copy
# hadoop.dll into C:\Windows\System32.
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["PATH"] = os.environ["HADOOP_HOME"] + r"\bin;" + os.environ["PATH"]

# ---------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------
BUCKET_NAME = "small-potato"
S3_FILE_PATH = "friday/bmw_customers.csv"
S3_URI = f"s3a://{BUCKET_NAME}/{S3_FILE_PATH}"
AWS_REGION = "us-west-2"

# Reports are written here, exactly as requested.
REPORTS_DIR = r"C:\Users\SKTamizhazhagan\OneDrive - BMW Techworks India Private Limited\Training\AWS\DAY-36\small-potato\src\modules\reports"


def build_spark_session() -> SparkSession:
    builder = (
        SparkSession.builder
        .appName("BMWCustomerRDDAnalysis")
        # hadoop-aws must match your Hadoop client version (3.5.0), and
        # Hadoop 3.4+ uses the AWS SDK v2 "bundle" artifact instead of
        # the old aws-java-sdk-bundle (SDK v1).
        .config("spark.jars.packages",
                "org.apache.hadoop:hadoop-aws:3.5.0,software.amazon.awssdk:bundle:2.35.4")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.endpoint.region", AWS_REGION)
    )

    # Reuse the same credentials your boto3 upload script already uses.
    access_key = os.environ.get("AWS_ACCESS_KEY_ID")
    secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    session_token = os.environ.get("AWS_SESSION_TOKEN")

    if access_key and secret_key:
        builder = (
            builder
            .config("spark.hadoop.fs.s3a.access.key", access_key)
            .config("spark.hadoop.fs.s3a.secret.key", secret_key)
        )
        if session_token:
            builder = (
                builder
                .config("spark.hadoop.fs.s3a.session.token", session_token)
                .config(
                    "spark.hadoop.fs.s3a.aws.credentials.provider",
                    "org.apache.hadoop.fs.s3a.auth.MarshalledCredentialProvider",
                )
            )
        else:
            builder = builder.config(
                "spark.hadoop.fs.s3a.aws.credentials.provider",
                "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
            )
    else:
        print(
            "WARNING: AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY not found in "
            "the environment. Set them (same ones your boto3 script uses) "
            "before running, or S3 access will fail."
        )

    spark = builder.getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    return spark


# ---------------------------------------------------------------------
# Step 1: Read the CSV from S3
# ---------------------------------------------------------------------
def read_customers_df(spark: SparkSession):
    """Read the raw CSV from S3 into a DataFrame (gives us a clean,
    typed starting point before we drop down to RDD operations)."""
    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(S3_URI)
    )
    print(f"Loaded {df.count()} rows from {S3_URI}")
    df.printSchema()
    return df


# ---------------------------------------------------------------------
# Step 2: RDD analyses
# ---------------------------------------------------------------------
def customer_count_by_city(df):
    """RDD map + reduceByKey: number of customers per city."""
    rdd = df.rdd.map(lambda row: (row["city"], 1))
    counts = rdd.reduceByKey(lambda a, b: a + b)
    return counts  # RDD[(city, count)]


def avg_purchase_price_by_model(df):
    """RDD map + reduceByKey: average purchase price per BMW model."""
    rdd = df.rdd.map(lambda row: (row["model"], (row["purchase_price_inr"], 1)))
    summed = rdd.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
    averages = summed.mapValues(lambda v: round(v[0] / v[1], 2))
    return averages  # RDD[(model, avg_price)]


def avg_income_by_customer_segment(df):
    """RDD map + reduceByKey: average annual income per customer segment."""
    rdd = df.rdd.map(lambda row: (row["customer_segment"], (row["annual_income_inr"], 1)))
    summed = rdd.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
    averages = summed.mapValues(lambda v: round(v[0] / v[1], 2))
    return averages  # RDD[(segment, avg_income)]


def high_value_customers(df, min_purchase_price: int = 15_000_000):
    """RDD filter: customers whose purchase price is above a threshold."""
    rdd = df.rdd.filter(lambda row: row["purchase_price_inr"] > min_purchase_price)
    projected = rdd.map(
        lambda row: (
            row["customer_id"],
            row["first_name"] + " " + row["last_name"],
            row["model"],
            row["city"],
            row["purchase_price_inr"],
        )
    )
    return projected  # RDD[(customer_id, name, model, city, price)]


def fuel_type_distribution(df):
    """RDD map + reduceByKey: customer count by fuel type."""
    rdd = df.rdd.map(lambda row: (row["fuel_type"], 1))
    counts = rdd.reduceByKey(lambda a, b: a + b)
    return counts  # RDD[(fuel_type, count)]


def avg_satisfaction_by_service_plan(df):
    """RDD map + reduceByKey: average satisfaction score per service plan."""
    rdd = df.rdd.map(lambda row: (row["service_plan"], (row["satisfaction_score"], 1)))
    summed = rdd.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
    averages = summed.mapValues(lambda v: round(v[0] / v[1], 3))
    return averages  # RDD[(service_plan, avg_satisfaction)]


# ---------------------------------------------------------------------
# Step 3: Write each result as ONE local Parquet file (not a folder of
# part-files). Spark always writes to a folder internally, so we
# coalesce to a single partition, then move that one part-file out to
# a clean "<name>.parquet" path and clean up the temp folder.
# ---------------------------------------------------------------------
def _write_single_parquet_file(df, out_file_path: str) -> None:
    tmp_dir = out_file_path + "__tmp"

    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    df.coalesce(1).write.mode("overwrite").parquet(tmp_dir)

    part_files = glob.glob(os.path.join(tmp_dir, "part-*.parquet"))
    if not part_files:
        raise RuntimeError(f"No part-file found in {tmp_dir} after write")

    if os.path.exists(out_file_path):
        os.remove(out_file_path)
    shutil.move(part_files[0], out_file_path)

    shutil.rmtree(tmp_dir)


def write_key_value_report(spark, rdd, key_name: str, value_name: str, value_type, folder: str):
    schema = StructType([
        StructField(key_name, StringType(), True),
        StructField(value_name, value_type, True),
    ])
    df = spark.createDataFrame(rdd, schema)
    out_file_path = os.path.join(REPORTS_DIR, f"{folder}.parquet")
    _write_single_parquet_file(df, out_file_path)
    print(f"Wrote {folder} -> {out_file_path}")


def write_high_value_customers_report(spark, rdd, folder: str = "high_value_customers"):
    schema = StructType([
        StructField("customer_id", StringType(), True),
        StructField("customer_name", StringType(), True),
        StructField("model", StringType(), True),
        StructField("city", StringType(), True),
        StructField("purchase_price_inr", IntegerType(), True),
    ])
    df = spark.createDataFrame(rdd, schema)
    out_file_path = os.path.join(REPORTS_DIR, f"{folder}.parquet")
    _write_single_parquet_file(df, out_file_path)
    print(f"Wrote {folder} -> {out_file_path}")


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    os.makedirs(REPORTS_DIR, exist_ok=True)

    spark = build_spark_session()
    df = read_customers_df(spark)

    # Run the RDD analyses
    city_counts = customer_count_by_city(df)
    model_avg_price = avg_purchase_price_by_model(df)
    segment_avg_income = avg_income_by_customer_segment(df)
    high_value = high_value_customers(df)
    fuel_dist = fuel_type_distribution(df)
    satisfaction_by_plan = avg_satisfaction_by_service_plan(df)

    # Persist each as its own local Parquet report
    write_key_value_report(spark, city_counts, "city", "customer_count", IntegerType(), "customer_count_by_city")
    write_key_value_report(spark, model_avg_price, "model", "avg_purchase_price_inr", DoubleType(), "avg_purchase_price_by_model")
    write_key_value_report(spark, segment_avg_income, "customer_segment", "avg_annual_income_inr", DoubleType(), "avg_income_by_segment")
    write_high_value_customers_report(spark, high_value)
    write_key_value_report(spark, fuel_dist, "fuel_type", "customer_count", IntegerType(), "fuel_type_distribution")
    write_key_value_report(spark, satisfaction_by_plan, "service_plan", "avg_satisfaction_score", DoubleType(), "avg_satisfaction_by_service_plan")

    print(f"\nAll reports written under: {REPORTS_DIR}")
    spark.stop()


if __name__ == "__main__":
    main()