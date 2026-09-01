import os
import sys
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession


PROJECT_ROOT = Path(__file__).resolve().parents[3]
CHENNAI_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "chennai_plant.txt"
PUNE_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "pune_plant.txt"


def flatten_telemetry_line(line):
	"""Convert one telemetry line into one tuple for each field."""
	parts = line.split("#")
	vehicle_id = parts[0]
	telemetry_fields = parts[1:]

	flattened_fields = []
	for field in telemetry_fields:
		field_name, field_value = field.split(":", maxsplit=1)
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
	chennai_rdd = spark.sparkContext.textFile(str(CHENNAI_PATH))
	pune_rdd = spark.sparkContext.textFile(str(PUNE_PATH))

	telemetry_rdd = chennai_rdd.union(pune_rdd)
	flattened_rdd = telemetry_rdd.flatMap(flatten_telemetry_line)

	print(f"Chennai records: {chennai_rdd.count()}")
	print(f"Pune records: {pune_rdd.count()}")
	print(f"Combined telemetry records: {telemetry_rdd.count()}")

	print("Sample union records:")
	for record in telemetry_rdd.take(10):
		print(record)

	print(f"Flattened records: {flattened_rdd.count()}")
	print("Sample flattened records:")
	for record in flattened_rdd.take(10):
		print(record)
finally:
	spark.stop()