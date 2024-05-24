-- Snowflake schema creation script
CREATE OR REPLACE DATABASE ecommerce_db;
USE DATABASE ecommerce_db;

CREATE OR REPLACE SCHEMA product_schema;
USE SCHEMA product_schema;

CREATE OR REPLACE TABLE product_details (
    product_name STRING,
    product_price STRING,
    product_rating STRING,
    product_reviews STRING,
    url STRING,
    scrape_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
