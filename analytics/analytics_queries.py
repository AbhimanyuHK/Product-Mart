import snowflake.connector
import pandas as pd
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

def execute_query(query):
    conn = get_snowflake_connection()
    try:
        df = pd.read_sql(query, conn)
        return df
    finally:
        conn.close()

def get_top_rated_products(limit=10):
    query = f"""
    SELECT product_name, product_price, product_rating, product_reviews, url
    FROM product_details
    ORDER BY product_rating DESC, product_reviews DESC
    LIMIT {limit}
    """
    return execute_query(query)

def get_price_distribution():
    query = """
    SELECT product_price, COUNT(*) as count
    FROM product_details
    GROUP BY product_price
    ORDER BY product_price ASC
    """
    return execute_query(query)

def main():
    print("Top Rated Products:")
    top_rated_products = get_top_rated_products()
    print(top_rated_products)

    print("\nPrice Distribution:")
    price_distribution = get_price_distribution()
    print(price_distribution)

if __name__ == "__main__":
    main()
