# product-predictor-bestbuy
A Python project that scrapes product and review data from Best Buy, performs sentiment analysis on reviews, and predicts the most loved TVs.

## Features
- Scrapes TV product data using Best Buy's JSON API
- Cleans and structures the dataset for analysis
- Uses sentiment analysis (TextBlob) on user reviews
- Scores and ranks products based on rating, review count, and sentiment
- Interactive Streamlit dashboard for exploring top products


## Run the data pipeline:
```bash
pip install -r requirements.txt
python src/scraper.py
python src/clean_data.py
python src/predictor.py
