import os
import sys
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession


PROJECT_ROOT = Path(__file__).resolve().parents[3]
TELEMETRY_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_telemetry.txt"


def flatten_telemetry_line(line):
	"""Convert one telemetry line into one tuple for each field."""
	vehicle_id, telemetry = line.split("#", maxsplit=1)
	flattened_fields = []
	for field in telemetry.split(","):
		field_name, field_value = field.split("=", maxsplit=1)
		flattened_fields.append((vehicle_id, field_name, field_value))
	return flattened_fields


spark = (
	SparkSession.builder
	.appName("BMW Telemetry RDD FlatMap")
	.config("spark.sql.shuffle.partitions", "4")
	.master("local[*]")
	.getOrCreate()
)

try:
	telemetry_rdd = spark.sparkContext.textFile(str(TELEMETRY_PATH))
	flattened_rdd = telemetry_rdd.flatMap(flatten_telemetry_line)

	print(f"Telemetry records: {telemetry_rdd.count()}")
	print(f"Flattened records: {flattened_rdd.count()}")
	for record in flattened_rdd.take(10):
		print(record)
finally:
	spark.stop()
