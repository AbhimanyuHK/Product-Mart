### Data Ingestion

- **data_ingestion/kafka_config.py**: Contains Kafka configuration settings, including the bootstrap servers and topic name.
- **data_ingestion/kafka_producer.py**: Defines a function to publish messages to a Kafka topic. It includes a sample test to publish a sample product detail.
- **data_ingestion/kafka_consumer.py**: Defines a function to consume messages from a Kafka topic and includes a placeholder for further data processing logic.
- **data_ingestion/kafka_setup.sh**: Shell script to create a Kafka topic for storing product details.

### Usage

1. **Kafka Setup**:
   - Run the `kafka_setup.sh` script to create the Kafka topic.
     ```bash
     chmod +x data_ingestion/kafka_setup.sh
     ./data_ingestion/kafka_setup.sh
     ```

2. **Publish Data to Kafka**:
   - Use the `kafka_producer.py` script to publish scraped product data to the Kafka topic.
     ```bash
     python data_ingestion/kafka_producer.py
     ```

3. **Consume Data from Kafka**:
   - Use the `kafka_consumer.py` script to consume and process data from the Kafka topic.
     ```bash
     python data_ingestion/kafka_consumer.py
     ```

This setup will allow you to publish scraped product data to Kafka and then consume and process that data for further steps in your data pipeline.
