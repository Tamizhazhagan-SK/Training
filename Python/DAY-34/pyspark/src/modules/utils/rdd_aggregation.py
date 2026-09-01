import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession


UPLOADS_PATH = "hdfs://namenode:9000/data/vehicle_data.txt"


def extract_odometer_pair(line):
	"""Convert one telemetry line into (vehicle_id, odometer_km)."""
	vehicle_id, telemetry = line.split("#", maxsplit=1)
	fields = dict(pair.split("=", maxsplit=1) for pair in telemetry.split(","))
	return (vehicle_id, int(fields["odometer_km"]))


# spark = (
# 	SparkSession.builder
# 	.appName("BMW Telemetry RDD ReduceByKey")
# 	.config("spark.sql.shuffle.partitions", "4")
# 	.master("local[*]")
# 	.getOrCreate()
# )


spark = (
	SparkSession.builder
	.appName("BMW Telemetry RDD ReduceByKey")
	.config("spark.executor.memory", "2g")
	.config("spark.sql.shuffle.partitions", "4")
	.master("spark://spark-master:7077")
	.getOrCreate()
)



try:
	uploads_rdd = spark.sparkContext.textFile(UPLOADS_PATH)
	odometer_pairs_rdd = uploads_rdd.map(extract_odometer_pair)

	# Max odometer reading per vehicle (handles duplicate/re-uploaded records
	# without inflating the total, unlike a sum would)
	max_odometer_rdd = odometer_pairs_rdd.reduceByKey(lambda a, b: max(a, b))

	# --- Alternatives, if your exercise wants a different aggregation ---
	# Total across all uploads (will double-count duplicates):
	# sum_odometer_rdd = odometer_pairs_rdd.reduceByKey(lambda a, b: a + b)
	#
	# Average per vehicle (needs a two-step reduce: sum + count, then divide):
	# sum_count_rdd = odometer_pairs_rdd.mapValues(lambda v: (v, 1)) \
	#     .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
	# avg_odometer_rdd = sum_count_rdd.mapValues(lambda sc: sc[0] / sc[1])

	sorted_result = max_odometer_rdd.sortByKey()

	print(f"Raw records processed: {odometer_pairs_rdd.count()}")
	print(f"Distinct vehicles after reduceByKey: {sorted_result.count()}")

	print("Max odometer reading per vehicle:")
	for vehicle_id, odometer in sorted_result.take(10):
		print(f"{vehicle_id}: {odometer} km")
finally:
	spark.stop()