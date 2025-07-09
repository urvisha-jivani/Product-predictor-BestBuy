
import pandas as pd

def merge_sentiment(product_path='data/processed/products_scored.csv',
                    sentiment_path='data/processed/product_sentiment_summary.csv',
                    output_path='data/processed/products_final.csv'):
    
    # Load product score and sentiment summary
    products_df = pd.read_csv(product_path)
    sentiment_df = pd.read_csv(sentiment_path)

    # Merge on product name
    merged_df = pd.merge(products_df, sentiment_df, on='product_name', how='left')

    # Fill any missing sentiment scores with 0 (no reviews)
    merged_df['avg_sentiment'] = merged_df['avg_sentiment'].fillna(0)

    # Create a new final score using weighted formula
    merged_df['final_score'] = (
        merged_df['score'] * 0.7 +      # existing score from rating + reviews
        merged_df['avg_sentiment'] * 0.3  # sentiment influence
    )

    # Sort by final score
    merged_df = merged_df.sort_values(by='final_score', ascending=False)

    # Save to file
    merged_df.to_csv(output_path, index=False)
    print(f" Merged data with sentiment saved to: {output_path}")

    return merged_df

if __name__ == '__main__':
    df = merge_sentiment()
    print("\n Sample output:\n")
    print(df[['product_name', 'price', 'score', 'avg_sentiment', 'final_score']].head(10))
