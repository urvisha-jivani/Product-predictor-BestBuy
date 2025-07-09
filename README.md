# product-predictor-bestbuy
A Python-based project that scrapes TV product data from Best Buy, processes it, and predicts the most popular products based on customer ratings and review counts. It includes an interactive dashboard built with Streamlit to explore top-ranked TVs.

## Features
- Scrapes TV product data from Best Buy's public JSON API
- Cleans and structures raw product data
- Scores and ranks products using customer rating and review count
- Interactive Streamlit dashboard to view top products
- Modular pipeline with separate scripts for scraping, cleaning, scoring, and visualization


## 🛠️ Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/urvisha-jivani/Product-predictor-BestBuy.git
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

4. **Launch the dashboard:**

```bash
streamlit run app.py
```

