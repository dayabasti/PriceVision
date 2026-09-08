# PriceVision – Real Estate Analytics & Price Prediction

PriceVision is a group project that combines real-estate data analytics, interactive visualizations, machine-learning based price prediction, and property recommendations in a Streamlit application.

## Project Overview

The application helps users explore real-estate pricing patterns, analyze property characteristics, visualize location-based trends, and estimate property prices based on selected property features.

## Key Features

- 📊 Real-estate dataset exploration and analysis
- 📈 Interactive data visualizations
- 🗺️ Sector-level price-per-square-foot geographic visualization
- 🏠 Property price prediction using a trained ML pipeline
- 🤝 Similar apartment/property recommendations
- 📥 Full dataset download from the analytics dashboard

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Plotly
- WordCloud
- Pickle

## Analytics & Visualizations

The analytics dashboard includes:

- Dataset overview and sample data
- Missing-value inspection
- Average property price KPI
- Most expensive sector KPI
- Most common BHK KPI
- Sector price-per-square-foot map
- Feature word cloud
- Built-up area vs. price scatter plot
- BHK distribution pie chart
- BHK price comparison box plot
- Price distribution by property type
- Average price by sector

## Price Prediction

The prediction module accepts property-related inputs such as:

- Property type
- Sector
- Number of bedrooms
- Number of bathrooms
- Balconies
- Property age
- Built-up area
- Servant room
- Store room
- Furnishing type
- Luxury category
- Floor category

The selected inputs are passed through the project's trained prediction pipeline to generate an estimated property price.

## Property Recommendation

PriceVision also includes a recommendation module that uses location-distance information and multiple cosine-similarity matrices to identify nearby and similar properties.

## My Contribution

This was developed as a **group project**.

My primary contributions were:

- **Data Cleaning & Preprocessing** – prepared and structured the real-estate data for analysis and downstream use.
- **Exploratory Data Analysis (EDA)** – analyzed property characteristics and pricing patterns to identify useful insights and trends.
- **Data Visualization** – contributed to the creation of visualizations used to communicate pricing, BHK, property-type, sector, and location-based insights.

## Project Structure

```text
PriceVision/
│
├── app.py
├── requirements.txt
│
├── pages/
│   ├── 1_Price_Prediction.py
│   ├── 2_Data_Visualizations.py
│   └── 2_Apartment_Recommender.py
│
└── datasets/
    ├── data_viz1.csv
    ├── df.pkl
    ├── pipeline.pkl
    ├── location_distance.pkl
    ├── cosine_sim1.pkl
    ├── cosine_sim2.pkl
    ├── cosine_sim3.pkl
    └── feature_text.pkl
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd PriceVision
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

## Project Type

**Group Project | Real Estate Analytics | Machine Learning | Data Visualization | Streamlit**

## Demo

The original project was deployed as a Streamlit application on Hugging Face Spaces.

Hugging Face Space:
https://huggingface.co/spaces/aaditi26002/PriceVision
