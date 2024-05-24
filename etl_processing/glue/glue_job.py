import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
import boto3

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
logger = glueContext.get_logger()

# Configuration
KAFKA_TOPIC = 'product-details'
KAFKA_BOOTSTRAP_SERVERS = 'kafka-cluster-endpoint:9092'
SNOWFLAKE_DATABASE = 'YOUR_DATABASE'
SNOWFLAKE_SCHEMA = 'YOUR_SCHEMA'
SNOWFLAKE_WAREHOUSE = 'YOUR_WAREHOUSE'
SNOWFLAKE_USER = 'YOUR_USER'
SNOWFLAKE_PASSWORD = 'YOUR_PASSWORD'
SNOWFLAKE_ACCOUNT = 'YOUR_ACCOUNT'

# Read from Kafka
df = glueContext.create_dynamic_frame.from_options(
    connection_type="kafka",
    connection_options={
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "topic": KAFKA_TOPIC
    },
    format="json"
)

# Convert DynamicFrame to DataFrame for processing
df = df.toDF()

# Perform data cleaning and transformation
df = df.withColumnRenamed('name', 'product_name')\
    .withColumnRenamed('price', 'product_price')\
    .withColumnRenamed('rating', 'product_rating')\
    .withColumnRenamed('reviews', 'product_reviews')

# Write to Snowflake
sf_options = {
    "sfURL": f"{SNOWFLAKE_ACCOUNT}.snowflakecomputing.com",
    "sfDatabase": SNOWFLAKE_DATABASE,
    "sfSchema": SNOWFLAKE_SCHEMA,
    "sfWarehouse": SNOWFLAKE_WAREHOUSE,
    "sfRole": "YOUR_ROLE",
    "sfUser": SNOWFLAKE_USER,
    "sfPassword": SNOWFLAKE_PASSWORD
}

df.write.format("snowflake")\
    .options(**sf_options)\
    .option("dbtable", "PRODUCT_DETAILS")\
    .mode("overwrite")\
    .save()

logger.info("Data successfully written to Snowflake.")
