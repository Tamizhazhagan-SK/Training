import os
import sys
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession


PROJECT_ROOT = Path(__file__).resolve().parents[3]
UPLOADS_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "vehicle_data.txt"


def extract_three_columns(line):
	"""Pull out vehicle_id, model, and fuel_type from a raw telemetry line."""
	vehicle_id, telemetry = line.split("#", maxsplit=1)
	fields = dict(pair.split("=", maxsplit=1) for pair in telemetry.split(","))
	return (vehicle_id, fields["model"], fields["fuel_type"])


spark = (
	SparkSession.builder
	.appName("BMW Telemetry RDD Distinct")
	.config("spark.sql.shuffle.partitions", "4")
	.master("local[*]")
	.getOrCreate()
)

try:
	uploads_rdd = spark.sparkContext.textFile(str(UPLOADS_PATH))
	distinct_rdd = uploads_rdd.distinct()

	print(f"Raw uploaded records (with duplicates): {uploads_rdd.count()}")
	print(f"Distinct records after dedup: {distinct_rdd.count()}")

	# Trim to 3 columns and sort ascending by vehicle_id for a clean view
	raw_trimmed = uploads_rdd.map(extract_three_columns).sortBy(lambda row: row[0])
	distinct_trimmed = distinct_rdd.map(extract_three_columns).sortBy(lambda row: row[0])

	print("Sample raw records (vehicle_id, model, fuel_type):")
	for record in raw_trimmed.take(5):
		print(record)

	print("Sample distinct records (vehicle_id, model, fuel_type):")
	for record in distinct_trimmed.take(5):
		print(record)
finally:
	spark.stop()