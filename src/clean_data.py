# This script cleans the product data by selecting relevant columns and removing rows with missing ratings or review counts.

import pandas as pd

def clean_product_data(input_path='data/raw/products_raw.csv', output_path='data/processed/products_clean.csv'):
    df = pd.read_csv(input_path)

    print(df.head())  # Display the first few rows for verification

    # Keep only useful columns
    df_clean = df[[
        'name',
        'salePrice',
        'customerRating',
        'customerReviewCount',
        'productUrl'
    ]].copy()

    # Rename for clarity
    df_clean.rename(columns={
        'name': 'product_name',
        'salePrice': 'price',
        'customerRating': 'rating',
        'customerReviewCount': 'review_count',
        'productUrl': 'url'
    }, inplace=True)

    # Drop rows with missing price or rating
    df_clean.dropna(subset=['price', 'rating'], inplace=True)

    df_clean.to_csv(output_path, index=False)
    print(f" Cleaned data saved to {output_path}")

if __name__ == '__main__':
    clean_product_data()

