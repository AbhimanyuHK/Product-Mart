import requests
from bs4 import BeautifulSoup
import json

def scrape_flipkart_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product = {
            'name': soup.find('span', {'class': 'B_NuCI'}).text.strip(),
            'price': soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text.strip(),
            'rating': soup.find('div', {'class': '_3LWZlK'}).text.strip(),
            'reviews': soup.find('span', {'class': '_2_R_DZ'}).text.strip().split()[0],
            'url': url
        }
        return product
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    url = "https://www.flipkart.com/product-url"  # Example product URL
    product_details = scrape_flipkart_product(url)
    print(json.dumps(product_details, indent=4))
