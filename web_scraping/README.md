### Web Scraping

- **web_scraping/amazon_scraper.py**: This script scrapes product details from an Amazon product page. It uses `requests` to fetch the page content and `BeautifulSoup` to parse the HTML and extract the necessary details.
- **web_scraping/flipkart_scraper.py**: This script scrapes product details from a Flipkart product page, similar to the Amazon scraper.
- **web_scraping/scheduler/lambda_handler.py**: This AWS Lambda function is triggered by a CloudWatch event. It calls the Amazon and Flipkart scrapers, and publishes the scraped data to a Kafka topic.
- **web_scraping/scheduler/cloudwatch_event.json**: This is a sample CloudWatch event configuration to schedule the Lambda function. It triggers the Lambda function at specified intervals to perform web scraping.

This project structure and code snippets should help you set up the web scraping part of your data ingestion pipeline. You can further customize the URLs and scraping logic based on your specific requirements.
