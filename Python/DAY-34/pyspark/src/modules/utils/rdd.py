import os
from pathlib import Path

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

from pyspark import TaskContext
from pyspark.sql import SparkSession
from pyspark import SparkContext
sc = SparkContext(...)
sc.setLogLevel("FATAL")


PROJECT_ROOT = Path(__file__).resolve().parents[3]
CSV_PATH = PROJECT_ROOT / "src" / "modules" / "data" / "bmw_customers.csv"
SIMULATE_FAILURE = os.getenv("SIMULATE_FAILURE", "false").lower() == "true"


def simulate_failure(records):
    task_context = TaskContext.get()
    partition_id = task_context.partitionId()
    attempt_number = task_context.attemptNumber()

    print(
        f"Processing partition {partition_id}, "
        f"attempt {attempt_number}"
    )

    if SIMULATE_FAILURE and partition_id == 2 and attempt_number == 0:
        raise RuntimeError("Simulated error in partition 2")

    for record in records:
        yield record


spark = (
    SparkSession.builder
    .appName("BMW Customer RDD Example")
    .config("spark.sql.shuffle.partitions", "4")
    .master("local[*]")
    .getOrCreate()
)

try:
    context = spark.sparkContext
    raw_rdd = context.textFile(str(CSV_PATH), minPartitions=4)
    data_rdd = (
        raw_rdd.zipWithIndex()
        .filter(lambda record: record[1] > 0)
        .map(lambda record: record[0])
    )
    split_rdd = data_rdd.map(lambda line: line.split(","))

    record_count = split_rdd.count()
    num_partitions = split_rdd.getNumPartitions()
    print(f"Number of customer records: {record_count}")
    print(f"Number of partitions: {num_partitions}")

    if SIMULATE_FAILURE:
        failure_rdd = split_rdd.mapPartitions(simulate_failure)
        try:
            failure_rdd.count()
        except Exception as error:
            print(f"Expected partition failure: {error}")

        print(
            "After the simulated failure: "
            f"{failure_rdd.getNumPartitions()} partitions are still defined"
        )

    print(f"Records still available in the source RDD: {split_rdd.count()}")
finally:
    spark.stop()


