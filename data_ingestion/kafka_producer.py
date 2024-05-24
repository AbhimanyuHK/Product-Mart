from kafka import KafkaProducer
import json
import kafka_config

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=kafka_config.KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def publish_to_kafka(topic, value):
    producer = get_kafka_producer()
    producer.send(topic, value=value)
    producer.flush()

if __name__ == "__main__":
    # Test publishing a sample product detail
    sample_data = {
        "name": "Sample Product",
        "price": "19.99",
        "rating": "4.5",
        "reviews": "150",
        "url": "https://www.example.com/sample-product"
    }
    publish_to_kafka(kafka_config.KAFKA_TOPIC, sample_data)
    print("Published to Kafka:", sample_data)
