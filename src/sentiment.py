import pandas as pd
from textblob import TextBlob
import re

def clean_text(text):
    # Basic cleanup: remove HTML tags, special chars, etc.
    text = re.sub(r'<.*?>', '', str(text))
    text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)
    return text.strip().lower()

def analyze_sentiment(text):
    cleaned = clean_text(text)
    if not cleaned:
        return 0.0
    blob = TextBlob(cleaned)
    return blob.sentiment.polarity  # returns value between -1.0 to 1.0

def score_reviews(input_path='data/processed/tv_reviews.csv', output_path='data/processed/tv_reviews_scored.csv'):
    df = pd.read_csv(input_path)
    df['sentiment_score'] = df['review_text'].apply(analyze_sentiment)
    df.to_csv(output_path, index=False)
    print(f"Sentiment-scored reviews saved to {output_path}")
    return df

def aggregate_product_sentiment(df):
    grouped = df.groupby('product_name')['sentiment_score'].mean().reset_index()
    grouped.rename(columns={'sentiment_score': 'avg_sentiment'}, inplace=True)
    return grouped

if __name__ == '__main__':
    df = score_reviews()
    product_scores = aggregate_product_sentiment(df)
    print(product_scores.head())
