# This script cleans the product data by selecting relevant columns and removing rows with missing ratings or review counts.

import pandas as pd

def clean_product_data(input_path='data/raw/products_raw.csv', output_path='data/processed/products_clean.csv'):
    df = pd.read_csv(input_path)

    # Keep only useful columns
    df_clean = df[[
        'name',
        'salePrice',
        'customerReviewAverage',
        'customerReviewCount',
        'productUrl'
    ]].copy()

    # Rename for clarity
    df_clean.rename(columns={
        'name': 'product_name',
        'salePrice': 'price',
        'customerReviewAverage': 'rating',
        'customerReviewCount': 'review_count',
        'productUrl': 'url'
    }, inplace=True)

    df_clean.to_csv(output_path, index=False)
    print(f" Cleaned data saved to {output_path}")

if __name__ == '__main__':
    clean_product_data()

