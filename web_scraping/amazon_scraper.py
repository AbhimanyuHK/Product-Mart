import requests
from bs4 import BeautifulSoup
import json

def scrape_amazon_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product = {
            'name': soup.find('span', {'id': 'productTitle'}).text.strip(),
            'price': soup.find('span', {'id': 'priceblock_ourprice'}).text.strip(),
            'rating': soup.find('span', {'class': 'a-icon-alt'}).text.strip(),
            'reviews': soup.find('span', {'id': 'acrCustomerReviewText'}).text.strip(),
            'url': url
        }
        return product
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    url = "https://www.amazon.com/dp/B08N5WRWNW"  # Example product URL
    product_details = scrape_amazon_product(url)
    print(json.dumps(product_details, indent=4))
