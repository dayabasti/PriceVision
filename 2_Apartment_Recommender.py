| *import* streamlit *as* st                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------- |
| *import* pickle                                                                                                                 |
| *import* pandas *as* pd                                                                                                         |
| *import* numpy *as* np                                                                                                          |
|                                                                                                                                 |
| *# Set up the page*                                                                                                             |
| st.set\_page\_config(page\_title="Recommend Apartments")                                                                        |
|                                                                                                                                 |
| *# --------------------------*                                                                                                  |
| *# Intro Section*                                                                                                               |
| *# --------------------------*                                                                                                  |
| st.title("🏠 PriceVision Recommender System")                                                                                   |
| st.markdown("""                                                                                                                 |
| Welcome to the \*\*PriceVision Apartment Recommender\*\*!                                                                       |
| This tool helps you:                                                                                                            |
|                                                                                                                                 |
| - 🔍 \*\*Search\*\* for nearby apartments within a given radius.                                                                |
| - 🏡 \*\*Discover similar properties\*\* based on apartment features and location.                                              |
|                                                                                                                                 |
| Built using a combination of spatial and content-based filtering to give you the most relevant suggestions.                     |
| """)                                                                                                                            |
|                                                                                                                                 |
| *# Load data*                                                                                                                   |
| location\_df = pickle.load(*open*('datasets/location\_distance.pkl', 'rb'))                                                     |
| cosine\_sim1 = pickle.load(*open*('datasets/cosine\_sim1.pkl', 'rb'))                                                           |
| cosine\_sim2 = pickle.load(*open*('datasets/cosine\_sim2.pkl', 'rb'))                                                           |
| cosine\_sim3 = pickle.load(*open*('datasets/cosine\_sim3.pkl', 'rb'))                                                           |
|                                                                                                                                 |
| *# Recommender function*                                                                                                        |
| *def* *recommend\_properties\_with\_scores*(property\_name, top\_n=5):                                                          |
|     cosine\_sim\_matrix = 0.5 \* cosine\_sim1 + 0.8 \* cosine\_sim2 + 1 \* cosine\_sim3                                         |
|                                                                                                                                 |
|     sim\_scores = *list*(*enumerate*(cosine\_sim\_matrix[location\_df.index.get\_loc(property\_name)]))                         |
|     sorted\_scores = *sorted*(sim\_scores, key=*lambda* x: x[1], reverse=True)                                                  |
|                                                                                                                                 |
|     top\_indices = [i[0] *for* i *in* sorted\_scores[1\:top\_n + 1]]                                                            |
|     top\_scores = [i[1] *for* i *in* sorted\_scores[1\:top\_n + 1]]                                                             |
|                                                                                                                                 |
|     top\_properties = location\_df.index[top\_indices].tolist()                                                                 |
|                                                                                                                                 |
|     recommendations\_df = pd.DataFrame({                                                                                        |
|         'Property Name': top\_properties,                                                                                       |
|         'Similarity Score': [*round*(score, 3) *for* score *in* top\_scores]                                                    |
|     })                                                                                                                          |
|                                                                                                                                 |
|     *return* recommendations\_df                                                                                                |
|                                                                                                                                 |
| *# --------------------------*                                                                                                  |
| *# Section 1: Radius Filter*                                                                                                    |
| *# --------------------------*                                                                                                  |
| st.header("📍 Search Apartments by Location and Radius")                                                                        |
| st.markdown("Find apartments located within a specific radius from your chosen location.")                                      |
|                                                                                                                                 |
| selected\_location = st.selectbox('Choose a location:', *sorted*(location\_df.columns.to\_list()))                              |
|                                                                                                                                 |
| radius = st.number\_input('Enter radius (in kilometers):', min\_value=0.0, step=0.5)                                            |
|                                                                                                                                 |
| *if* st.button('Search'):                                                                                                       |
|     *try*:                                                                                                                      |
|         nearby\_apartments = location\_df[location\_df[selected\_location] < radius \* 1000][selected\_location].sort\_values() |
|         *if* nearby\_apartments.empty:                                                                                          |
|             st.warning("No apartments found within the selected radius.")                                                       |
|         *else*:                                                                                                                 |
|             st.subheader("🏘️ Apartments within radius:")                                                                       |
|             *for* apartment, distance *in* nearby\_apartments.items():                                                          |
|                 st.text(f"{apartment} - {*round*(distance / 1000, 2)} km")                                                      |
|     *except* KeyError:                                                                                                          |
|         st.error("Selected location not found in the dataset.")                                                                 |
|                                                                                                                                 |
| *# --------------------------*                                                                                                  |
| *# Section 2: Recommendations*                                                                                                  |
| *# --------------------------*                                                                                                  |
| st.header("🤝 Get Similar Apartment Recommendations")                                                                           |
| st.markdown("Select an apartment to discover similar properties based on features and location proximity.")                     |
|                                                                                                                                 |
| selected\_apartment = st.selectbox('Select an apartment:', *sorted*(location\_df.index.to\_list()))                             |
|                                                                                                                                 |
| *if* st.button('Recommend'):                                                                                                    |
|     recommendation\_df = recommend\_properties\_with\_scores(selected\_apartment)                                               |
|     st.subheader(f"Top Recommendations Similar to '{selected\_apartment}'")                                                     |
|     st.dataframe(recommendation\_df)                                                                                            |