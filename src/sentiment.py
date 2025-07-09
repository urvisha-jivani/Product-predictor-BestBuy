
import pandas as pd
from textblob import TextBlob
import re
import os

# Clean the text: remove HTML, symbols, etc.
def clean_text(text):
    text = re.sub(r'<.*?>', '', str(text))  # remove HTML
    text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)  # keep letters, numbers, punctuation
    return text.strip().lower()

# Calculate sentiment score from text
def analyze_sentiment(text):
    cleaned = clean_text(text)
    if not cleaned:
        return 0.0
    blob = TextBlob(cleaned)
    return blob.sentiment.polarity  # returns -1.0 to 1.0

# Step 1: Score individual reviews
def score_reviews(input_path='data/processed/product_reviews.csv',
                  output_path='data/processed/product_reviews_scored.csv'):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")
    
    if os.path.getsize(input_path) == 0:
        raise ValueError(f"File is empty: {input_path}")

    df = pd.read_csv(input_path)

    if 'review_text' not in df.columns or 'product_name' not in df.columns:
        raise ValueError("Columns 'review_text' and 'product_name' are required.")

    print("🔍 Scoring individual review sentiment...")
    df['sentiment_score'] = df['review_text'].apply(analyze_sentiment)

    df.to_csv(output_path, index=False)
    print(f"Saved individual sentiment scores to: {output_path}")
    return df

# Step 2: Aggregate sentiment by product
def aggregate_product_sentiment(df, output_path='data/processed/product_sentiment_summary.csv'):
    grouped = df.groupby('product_name')['sentiment_score'].mean().reset_index()
    grouped.rename(columns={'sentiment_score': 'avg_sentiment'}, inplace=True)
    grouped.to_csv(output_path, index=False)
    print(f"Saved average sentiment per product to: {output_path}")
    return grouped

if __name__ == '__main__':
    reviews_df = score_reviews()
    summary_df = aggregate_product_sentiment(reviews_df)

    print("\n Sample of averaged product sentiment:\n")
    print(summary_df.head())
