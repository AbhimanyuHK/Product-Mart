## Data Warehouse

- **data_warehouse/snowflake_schema.sql**: This SQL script creates a new database and schema in Snowflake and defines a table to store product details.
- **data_warehouse/snowflake_config.py**: Contains the configuration settings required to connect to Snowflake.
- **data_warehouse/snowflake_loader.py**: This script connects to Kafka to consume product data and loads it into the Snowflake table. It includes functions to establish a Snowflake connection and insert data into the Snowflake table.

### Usage

1. **Create Snowflake Schema**:
   - Execute the `snowflake_schema.sql` script in the Snowflake console or using a Snowflake client tool to create the database, schema, and table.
     ```bash
     snowflake -a your_snowflake_account -u your_snowflake_user -r your_role -q "source data_warehouse/snowflake_schema.sql"
     ```

2. **Load Data into Snowflake**:
   - Run the `snowflake_loader.py` script to start consuming data from Kafka and loading it into Snowflake.
     ```bash
     python data_warehouse/snowflake_loader.py
     ```

This setup will allow you to create the necessary Snowflake schema and load data into it from Kafka, completing the data ingestion pipeline from web scraping to data warehousing.
