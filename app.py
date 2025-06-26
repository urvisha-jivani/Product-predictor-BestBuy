import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/products_clean.csv')
    if 'avg_sentiment' in df.columns:
        df['score'] = (df['customerRating'] * 0.5 +
                       df['customerReviewCount'] * 0.3 +
                       df['avg_sentiment'] * 0.2)
    else:
        df['score'] = (df['customerRating'] * 0.6 +
                       df['customerReviewCount'] * 0.4)
    return df.sort_values(by='score', ascending=False)

df = load_data()

# App UI
st.title("Best Buy TV Product Predictor")
st.subheader("Ranked by Rating, Reviews, and Sentiment")

# Category filter
# st.selectbox("Select Category", options=["TVs"])

top_n = st.slider("Show Top N Products", min_value=5, max_value=50, value=10)

st.write("### Top Products")
st.dataframe(df[['name', 'salePrice', 'customerRating', 'customerReviewCount', 'score']].head(top_n))

# Optional: Chart
st.write("### Ratings vs. Review Count")
st.scatter_chart(df.head(top_n)[['customerRating', 'customerReviewCount']])
