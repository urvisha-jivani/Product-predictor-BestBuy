import requests
import json
import time
import os
import pandas as pd


print("Starting Best Buy TV Products Scraper...")

# This script scrapes TV product data from Best Buy Canada using their public API.

def scrape_bestbuy_products(pages=5, page_size=24, region='ON'):

    base_url = "https://www.bestbuy.ca/api/v2/json/search"
    all_products = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }

    for page in range(1, pages + 1):

        print(f"Scraping page {page}...")
        
        params = {
            "categoryid": "20003",
            "currentRegion": region,
            "page": page,
            "pageSize": page_size
        }

        for attempt in range(2):  # try up to 2 times
            try:
                res = requests.get(base_url, params=params, headers=headers, timeout=10)
                res.raise_for_status()
                data = res.json()
                products = data.get("products", [])
                all_products.extend(products)
                break  # success
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(3)  # wait before retrying
        else:
            print(f"Skipping page {page} after 2 failed attempts.")

        time.sleep(1)  # Delay between requests to avoid hitting the server too hard

    return all_products

# Save the scraped products to a CSV file

def save_products_to_csv(products, filename='data/raw/products_raw.csv'):
    df = pd.DataFrame(products)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

    print(f"Saved {len(df)} products to {filename}")

# Main function to run the scraper and save the data

if __name__ == '__main__':

    print("Starting the scraper...")

    products = scrape_bestbuy_products(pages=5)

    print(f"Total products scraped: {len(products)}")

    save_products_to_csv(products)