import json
import boto3
from datetime import datetime
from amazon_scraper import scrape_amazon_product
from flipkart_scraper import scrape_flipkart_product

kafka_topic = "product-details"
kafka_bootstrap_servers = "kafka-cluster-endpoint:9092"

def publish_to_kafka(topic, value):
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send(topic, value=value)
    producer.flush()

def lambda_handler(event, context):
    amazon_urls = event.get("amazon_urls", [])
    flipkart_urls = event.get("flipkart_urls", [])

    for url in amazon_urls:
        try:
            product_details = scrape_amazon_product(url)
            publish_to_kafka(kafka_topic, product_details)
        except Exception as e:
            print(f"Failed to scrape Amazon URL {url}: {str(e)}")

    for url in flipkart_urls:
        try:
            product_details = scrape_flipkart_product(url)
            publish_to_kafka(kafka_topic, product_details)
        except Exception as e:
            print(f"Failed to scrape Flipkart URL {url}: {str(e)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Scraping completed at ' + str(datetime.utcnow()))
    }
