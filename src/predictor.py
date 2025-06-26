import pandas as pd

# This script scores TV products based on customer ratings and review counts, and prints the top 10 products.
def score_products(data_path='data/processed/products_clean.csv'):
    df = pd.read_csv(data_path)
    df['score'] = (df['customerRating'] * 0.6) + (df['customerReviewCount'] * 0.4)
    top_products = df.sort_values(by='score', ascending=False)
    print(top_products[['name', 'salePrice', 'score']].head(10))
    return top_products

if __name__ == '__main__':
    score_products()
