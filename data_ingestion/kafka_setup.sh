#!/bin/bash

# Kafka setup script to create the required topic
KAFKA_TOPIC="product-details"
KAFKA_BOOTSTRAP_SERVERS="kafka-cluster-endpoint:9092"

# Create Kafka topic
kafka-topics --create --topic $KAFKA_TOPIC --bootstrap-server $KAFKA_BOOTSTRAP_SERVERS --replication-factor 1 --partitions 1

echo "Kafka topic '$KAFKA_TOPIC' created successfully."
