import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/products_clean.csv')
    df['rating'] = df['rating'].fillna(0)
    df['review_count'] = df['review_count'].fillna(0)
    df['price'] = df['price'].fillna(0)
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Products")

# Search
search_term = st.sidebar.text_input("Search product name")

# Price range
min_price, max_price = int(df['price'].min()), int(df['price'].max())
price_range = st.sidebar.slider("Price range", min_price, max_price, (min_price, max_price))

# Price and Product filters
filtered_df = df[
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1]) &
    (df['product_name'].str.contains(search_term, case=False, na=False))
].copy()

# Compute score
filtered_df['score'] = (filtered_df['rating'] * 0.6 + filtered_df['review_count'] * 0.4)

# Sort products
filtered_df = filtered_df.sort_values(by='score', ascending=False)

# Main content
st.title("Best Buy TV Product Predictor")
st.subheader("Ranked by Customer Rating and Review Count")

top_n = st.slider("Show Top N Products", min_value=5, max_value=50, value=10)

st.markdown("### Top Products")

# Make product name clickable
filtered_df['product_link'] = filtered_df.apply(
    lambda row: f"[{row['product_name']}]({row['url']})", axis=1
)

# Display table
# Prepare display DataFrame
styled_df = filtered_df[['product_link', 'price', 'rating', 'review_count', 'score']].rename(columns={
    'product_link': 'Product',
    'price': 'Price ($)',
    'rating': 'Rating',
    'review_count': 'Review Count',
    'score': 'Score'
}).head(top_n)

# Format numeric values
styled_df['Price ($)'] = styled_df['Price ($)'].map('${:,.2f}'.format)
styled_df['Rating'] = styled_df['Rating'].round(1)
styled_df['Score'] = styled_df['Score'].round(2)

# Display with Streamlit DataFrame UI
st.dataframe(
    styled_df,
    use_container_width=True,
    hide_index=True
)


# Visualization
st.markdown("### Ratings vs Review Count")
st.scatter_chart(filtered_df.head(top_n)[['rating', 'review_count']])
