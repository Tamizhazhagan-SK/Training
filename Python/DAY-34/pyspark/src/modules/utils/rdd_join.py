import os
import sys
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession


PROJECT_ROOT = Path(__file__).resolve().parents[3]
MASTER_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_model_master.csv"
SALES_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_sales_data.csv"

SALES_FIELDS = ["sale_id", "dealer_city", "sale_date", "sale_price_inr", "customer_type"]
MASTER_FIELDS = ["segment", "fuel_type", "body_type", "base_price_inr", "launch_year"]


def parse_master_row(line):
	"""(model, (segment, fuel_type, body_type, base_price_inr, launch_year))"""
	model, segment, fuel_type, body_type, base_price_inr, launch_year = line.split(",")
	return (model, (segment, fuel_type, body_type, int(base_price_inr), int(launch_year)))


def parse_sales_row(line):
	"""(model, (sale_id, dealer_city, sale_date, sale_price_inr, customer_type))"""
	sale_id, model, dealer_city, sale_date, sale_price_inr, customer_type = line.split(",")
	return (model, (sale_id, dealer_city, sale_date, int(sale_price_inr), customer_type))


def flatten_joined_record(record):
	"""Turn one joined (model, (sales_tuple, master_tuple)) record into
	multiple (model, field_name, field_value) rows — one per field
	across BOTH the sales side and the master side."""
	model, (sales_tuple, master_tuple) = record
	flattened_fields = []

	for field_name, field_value in zip(SALES_FIELDS, sales_tuple):
		flattened_fields.append((model, field_name, field_value))

	for field_name, field_value in zip(MASTER_FIELDS, master_tuple):
		flattened_fields.append((model, field_name, field_value))

	return flattened_fields


spark = (
	SparkSession.builder
	.appName("BMW Sales-Master RDD Join")
	.config("spark.sql.shuffle.partitions", "4")
	.master("local[*]")
	.getOrCreate()
)

try:
	master_raw = spark.sparkContext.textFile(str(MASTER_PATH))
	sales_raw = spark.sparkContext.textFile(str(SALES_PATH))

	master_header = master_raw.first()
	sales_header = sales_raw.first()

	master_rdd = master_raw.filter(lambda line: line != master_header).map(parse_master_row)
	sales_rdd = sales_raw.filter(lambda line: line != sales_header).map(parse_sales_row)

	joined_rdd = sales_rdd.join(master_rdd)
	flattened_rdd = joined_rdd.flatMap(flatten_joined_record)

	print(f"Master records: {master_rdd.count()}")
	print(f"Sales records: {sales_rdd.count()}")
	print(f"Joined records: {joined_rdd.count()}")
	print(f"Flattened records: {flattened_rdd.count()}")

	print("Sample joined records (model, (sales_data, master_data)):")
	for record in joined_rdd.take(3):
		print(record)

	print("Sample flattened records (model, field_name, field_value):")
	for record in flattened_rdd.take(10):
		print(record)
finally:
	spark.stop()