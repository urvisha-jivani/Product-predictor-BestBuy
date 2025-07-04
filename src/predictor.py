import pandas as pd

# This script scores TV products based on customer ratings and review counts, and prints the top 10 products.

def score_products(data_path='data/processed/products_clean.csv',
                   output_path='data/processed/products_scored.csv'):
    
    # Load cleaned product data
    df = pd.read_csv(data_path)

    # Fill missing values if any
    df[['rating', 'review_count']] = df[['rating', 'review_count']].fillna(0)

    # Score formula: weighted rating and review count
    df['score'] = (df['rating'] * 0.6) + (df['review_count'] * 0.4)

    # Sort by score
    top_products = df.sort_values(by='score', ascending=False)

    # Show top 10
    print("\n Top 10 Scored Products:\n")
    print(top_products[['product_name', 'price', 'score']].head(10))

    # Save the scored products
    top_products.to_csv(output_path, index=False)
    print(f"\n Scored products saved to {output_path}")

    return top_products

if __name__ == '__main__':
    score_products()
