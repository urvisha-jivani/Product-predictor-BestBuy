import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/products_clean.csv')

    # Check and handle missing values
    df['rating'] = df['rating'].fillna(0)
    df['review_count'] = df['review_count'].fillna(0)

    # Calculate score
    if 'avg_sentiment' in df.columns:
        df['score'] = (df['rating'] * 0.5 +
                       df['review_count'] * 0.3 +
                       df['avg_sentiment'] * 0.2)
    else:
        df['score'] = (df['rating'] * 0.6 +
                       df['review_count'] * 0.4)

    return df.sort_values(by='score', ascending=False)

df = load_data()

# App UI
st.title("Best Buy TV Product Predictor")
st.subheader("Top TVs Ranked by Ratings and Reviews")

top_n = st.slider("Number of Products to Display", min_value=5, max_value=50, value=10)

st.write("### Top Products")
st.dataframe(df[['product_name', 'price', 'rating', 'review_count', 'score']].head(top_n))

# Visualization
st.write("### Rating vs. Review Count")
st.scatter_chart(df.head(top_n)[['rating', 'review_count']])
