## Analytics

- **analytics/snowflake_config.py**: Contains Snowflake configuration settings required to connect to Snowflake.
- **analytics/analytics_queries.py**: This script defines functions to query Snowflake and perform basic analytics. It includes functions to get the top-rated products and the price distribution of the products.
  - **get_snowflake_connection()**: Establishes a connection to Snowflake.
  - **execute_query(query)**: Executes a given SQL query and returns the result as a Pandas DataFrame.
  - **get_top_rated_products(limit)**: Retrieves the top-rated products based on ratings and reviews.
  - **get_price_distribution()**: Retrieves the price distribution of the products.
  - **main()**: Main function to print the results of the analytics queries.
- **analytics/requirements.txt**: Specifies the dependencies for the analytics script.

### Usage

1. **Install Dependencies**:
   - Navigate to the `analytics` directory and install the required dependencies using pip.
     ```bash
     cd analytics
     pip install -r requirements.txt
     ```

2. **Run Analytics Script**:
   - Run the `analytics_queries.py` script to perform the analytics queries and print the results.
     ```bash
     python analytics_queries.py
     ```

This setup will allow you to perform basic analytics on the data stored in Snowflake, such as retrieving the top-rated products and analyzing the price distribution of the products. You can expand the script with additional queries and analytics as needed for your use case.
