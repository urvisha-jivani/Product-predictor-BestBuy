import requests
import json
import time
import os
import pandas as pd


print("Starting Best Buy TV Products Scraper...")

def scrape_bestbuy_tv_products(pages=5, page_size=24, region='ON'):

    base_url = "https://www.bestbuy.ca/api/v2/json/search"
    all_products = []

    for page in range(1, pages + 1):

        params = {
            "categoryid": "20003",
            "currentRegion": region,
            "page": page,
            "pageSize": page_size
        }
        res = requests.get(base_url, params=params)

        if res.status_code != 200:
            print(f"Failed to fetch page {page}")
            continue

        data = res.json()
        products = data.get("products", [])
        all_products.extend(products)

        time.sleep(1)   # Scraping with a delay

    return all_products

def save_products_to_csv(products, filename='data/raw/products_raw.csv'):
    df = pd.DataFrame(products)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} products to {filename}")

if __name__ == '__main__':
    products = scrape_bestbuy_tv_products(pages=10)
    save_products_to_csv(products)