# product-predictor-bestbuy
A Python project that scrapes product and review data from Best Buy, performs sentiment analysis on reviews, and predicts the most loved TVs.

## Features
- Scrapes TV product data using Best Buy's JSON API
- Cleans and structures the dataset for analysis
- Uses sentiment analysis (TextBlob) on user reviews
- Scores and ranks products based on rating, review count, and sentiment
- Interactive Streamlit dashboard for exploring top products

## 🛠️ Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/urvisha-jivani/product-predictor-bestbuy.git
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the data pipeline:**

```bash
python src/scraper.py
python src/clean_data.py
python src/predictor.py
```
