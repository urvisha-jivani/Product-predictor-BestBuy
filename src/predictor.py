import pandas as pd
import os

# This script scores TV products based on customer ratings and review counts, and prints the top 10 products.

def score_products(data_path='data/processed/products_clean.csv',
                   output_path='data/processed/products_scored.csv'):
    # Check if input file exists
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Input file not found: {data_path}")

    # Load cleaned product data
    df = pd.read_csv(data_path)

    # Ensure required columns are present
    required_cols = ['product_name', 'rating', 'review_count', 'price']
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in input data: {missing}")

    # Fill missing values
    df[['rating', 'review_count']] = df[['rating', 'review_count']].fillna(0)

    # Calculate score: weighted combination of rating and review count
    df['score'] = (df['rating'] * 0.6) + (df['review_count'] * 0.4)

    # Sort by score descending
    top_products = df.sort_values(by='score', ascending=False)

    # Print top 10 products
    print("Top 10 scored products:")
    print(top_products[['product_name', 'price', 'score']].head(10))

    # Save scored products to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    top_products.to_csv(output_path, index=False)
    print(f"Scored product data saved to: {output_path}")

    return top_products

if __name__ == '__main__':
    score_products()
