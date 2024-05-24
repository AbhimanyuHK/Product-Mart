import snowflake.connector
import json
from kafka import KafkaConsumer
import kafka_config
import snowflake_config

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user=snowflake_config.SNOWFLAKE_USER,
        password=snowflake_config.SNOWFLAKE_PASSWORD,
        account=snowflake_config.SNOWFLAKE_ACCOUNT,
        warehouse=snowflake_config.SNOWFLAKE_WAREHOUSE,
        database=snowflake_config.SNOWFLAKE_DATABASE,
        schema=snowflake_config.SNOWFLAKE_SCHEMA,
        role=snowflake_config.SNOWFLAKE_ROLE
    )
    return conn

def load_data_to_snowflake(data):
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    try:
        insert_query = """
        INSERT INTO product_details (product_name, product_price, product_rating, product_reviews, url)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            data['product_name'],
            data['product_price'],
            data['product_rating'],
            data['product_reviews'],
            data['url']
        ))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def consume_from_kafka():
    consumer = KafkaConsumer(
        kafka_config.KAFKA_TOPIC,
        bootstrap_servers=kafka_config.KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='snowflake-loader-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        product_data = message.value
        print("Consumed from Kafka:", product_data)
        load_data_to_snowflake(product_data)

if __name__ == "__main__":
    consume_from_kafka()
