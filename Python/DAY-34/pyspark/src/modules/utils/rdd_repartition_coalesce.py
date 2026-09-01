import os
import sys
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession


PROJECT_ROOT = Path(__file__).resolve().parents[3]
UPLOADS_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "vehicle_data.txt"


def show_partition_sizes(rdd, label):
	"""glom() collects each partition's records into a single list, so we
	can see exactly how many records landed in each partition."""
	sizes = rdd.glom().map(len).collect()
	print(f"{label}: {rdd.getNumPartitions()} partitions, sizes = {sizes}")


spark = (
	SparkSession.builder
	.appName("BMW Telemetry RDD Repartition")
	.config("spark.sql.shuffle.partitions", "4")
	.master("local[*]")
	.getOrCreate()
)

try:
	uploads_rdd = spark.sparkContext.textFile(str(UPLOADS_PATH))

	print(f"Total records: {uploads_rdd.count()}")
	show_partition_sizes(uploads_rdd, "Original partitioning")

	# --- repartition UP: more partitions, more parallelism ---
	# Triggers a full shuffle; data is redistributed roughly evenly.
	more_partitions_rdd = uploads_rdd.repartition(8)
	show_partition_sizes(more_partitions_rdd, "After repartition(8)")

	# --- repartition DOWN: fewer partitions ---
	# Also a full shuffle even though we're reducing count, since
	# repartition() always shuffles regardless of direction.
	fewer_partitions_rdd = uploads_rdd.repartition(2)
	show_partition_sizes(fewer_partitions_rdd, "After repartition(2)")

	# --- coalesce DOWN: fewer partitions, NO shuffle ---
	# Cheaper than repartition(2) for reducing partition count, but can
	# leave partitions uneven since it just merges existing ones locally.
	coalesced_rdd = uploads_rdd.coalesce(2)
	show_partition_sizes(coalesced_rdd, "After coalesce(2)")

	# Sanity check: record count must be identical no matter how it's partitioned
	print(f"\nRecord count unchanged after repartition(8): {more_partitions_rdd.count()}")
	print(f"Record count unchanged after repartition(2): {fewer_partitions_rdd.count()}")
	print(f"Record count unchanged after coalesce(2): {coalesced_rdd.count()}")
finally:
	spark.stop()