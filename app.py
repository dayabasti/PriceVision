| *import* streamlit *as* st                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *import* os                                                                                                                                                                     |
|                                                                                                                                                                                 |
| *# Set page config*                                                                                                                                                             |
| st.set\_page\_config(                                                                                                                                                           |
|     page\_title="PriceVision \| Real Estate Analytics & Prediction",                                                                                                            |
|     page\_icon="🏠",                                                                                                                                                            |
|     layout="wide"                                                                                                                                                               |
| )                                                                                                                                                                               |
|                                                                                                                                                                                 |
| *# --- Logo Section (with fallback) ---*                                                                                                                                        |
| st.markdown("\<h1 style='text-align: center;'>🏠 Welcome to \<span style='color:#6c63ff'>PriceVision\</span>\</h1>", unsafe\_allow\_html=True)                                  |
|                                                                                                                                                                                 |
| *# Load logo image if available*                                                                                                                                                |
| logo\_path = "assets/logo.png"                                                                                                                                                  |
| *if* os.path.exists(logo\_path):                                                                                                                                                |
|     st.image(logo\_path, width=120)                                                                                                                                             |
| *else*:                                                                                                                                                                         |
|     st.image("https\://cdn-icons-png.flaticon.com/512/2356/2356787.png", width=80)                                                                                              |
|                                                                                                                                                                                 |
| *# --- Greeting Input ---*                                                                                                                                                      |
| user = st.text\_input("👋 Enter your name to personalize your experience:")                                                                                                     |
| *if* user:                                                                                                                                                                      |
|     st.balloons()                                                                                                                                                               |
|     st.success(f"Welcome aboard, {user}! 🚀 Start exploring real estate insights with PriceVision.")                                                                            |
|                                                                                                                                                                                 |
| *# --- Description ---*                                                                                                                                                         |
| st.markdown("### Your Intelligent Real Estate Price Prediction & Analytics Dashboard")                                                                                          |
|                                                                                                                                                                                 |
| st.write("""                                                                                                                                                                    |
| \*\*PriceVision\*\* is a data-driven application designed to \*\*analyze\*\*, \*\*predict\*\*, and \*\*visualize\*\* real estate trends using advanced machine learning models. |
|                                                                                                                                                                                 |
| Whether you're a \*\*homebuyer, investor, or realtor\*\*, PriceVision helps you:                                                                                                |
| - 📊 \*\*Understand pricing patterns\*\* across different sectors                                                                                                               |
| - 🤖 \*\*Predict property prices\*\* using multiple regression models                                                                                                           |
| - 🧠 \*\*Gain insights\*\* into key real estate features that influence price                                                                                                   |
| - 📍 Explore \*\*location-based analytics\*\* for smarter decision-making                                                                                                       |
| """)                                                                                                                                                                            |
|                                                                                                                                                                                 |
| *# --- Key Features (Accordion) ---*                                                                                                                                            |
| *with* st.expander("🔍 View Key Features"):                                                                                                                                     |
|     st.markdown("""                                                                                                                                                             |
|     ### 🧠 Key Features:                                                                                                                                                        |
|     - 🧮 \*\*Price Prediction\*\* using ML models like Random Forest, XGBoost, Ridge, and more                                                                                  |
|     - 🌍 \*\*Interactive Visualizations\*\* of property data (box plots, heatmaps, pie charts)                                                                                  |
|     - 🧠 \*\*Recommendation System\*\* to suggest similar properties                                                                                                            |
|     """)                                                                                                                                                                        |
|                                                                                                                                                                                 |
| *# --- Navigation Buttons (Multipage Routing) ---*                                                                                                                              |
| col1, col2 = st.columns([1, 2])                                                                                                                                                 |
| *with* col1:                                                                                                                                                                    |
|     *if* st.button("📈 Go to Price Prediction"):                                                                                                                                |
|         st.switch\_page("pages/1\_Price\_Prediction")                                                                                                                           |
| *with* col2:                                                                                                                                                                    |
|     *if* st.button("🌍 Explore Data Visualizations"):                                                                                                                           |
|         st.switch\_page("pages/2\_Data\_Visualizations")                                                                                                                        |
|                                                                                                                                                                                 |
| *# --- Footer ---*                                                                                                                                                              |
| st.markdown("""                                                                                                                                                                 |
| \<hr style="border: 1px solid #ddd;">                                                                                                                                           |
| \<div style='text-align: center; font-size: 14px; color: gray;'>                                                                                                                |
|     © 2025 PriceVision \| Built with ❤️ using Streamlit                                                                                                                         |
| \</div>                                                                                                                                                                         |
| """, unsafe\_allow\_html=True)                                                                                                                                                  |