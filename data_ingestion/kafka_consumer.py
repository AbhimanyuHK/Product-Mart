from kafka import KafkaConsumer
import json
import kafka_config

def get_kafka_consumer():
    return KafkaConsumer(
        kafka_config.KAFKA_TOPIC,
        bootstrap_servers=kafka_config.KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='product-details-consumers',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

def consume_from_kafka():
    consumer = get_kafka_consumer()
    for message in consumer:
        product_data = message.value
        # Process the consumed data (e.g., print or save to database)
        print("Consumed from Kafka:", product_data)
        # Placeholder for further processing of the data
        process_data(product_data)

def process_data(data):
    # Placeholder for data processing logic
    print("Processing data:", data)

if __name__ == "__main__":
    consume_from_kafka()
