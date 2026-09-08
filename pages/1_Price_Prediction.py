| *import* streamlit *as* st                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *import* pickle                                                                                                                                                                     |
| *import* pandas *as* pd                                                                                                                                                             |
| *import* numpy *as* np                                                                                                                                                              |
|                                                                                                                                                                                     |
| st.set\_page\_config(page\_title="Viz Demo")                                                                                                                                        |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
| *with* *open*('df.pkl','rb') *as* file:                                                                                                                                             |
|     df = pickle.load(file)                                                                                                                                                          |
|                                                                                                                                                                                     |
| *with* *open*('pipeline.pkl','rb') *as* file:                                                                                                                                       |
|     pipeline = pickle.load(file)                                                                                                                                                    |
|                                                                                                                                                                                     |
| *# Section Header for Price Prediction*                                                                                                                                             |
| st.markdown("---")                                                                                                                                                                  |
| st.markdown("## 🧮 Price Prediction Module")                                                                                                                                        |
| st.write("""                                                                                                                                                                        |
| Use this module to predict real estate prices based on key property features such as:                                                                                               |
| - 📐 Built-up area                                                                                                                                                                  |
| - 🛏️ Number of bedrooms and bathrooms                                                                                                                                              |
| - 🏢 Floor category, furnishing type, luxury segment                                                                                                                                |
| - 📍 Sector and property type                                                                                                                                                       |
| """)                                                                                                                                                                                |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
| st.header('Enter your inputs')                                                                                                                                                      |
|                                                                                                                                                                                     |
| *# property\_type*                                                                                                                                                                  |
| property\_type = st.selectbox('Property Type',['flat','house'])                                                                                                                     |
|                                                                                                                                                                                     |
| *# sector*                                                                                                                                                                          |
| sector = st.selectbox('Sector',*sorted*(df['sector'].unique().tolist()))                                                                                                            |
|                                                                                                                                                                                     |
| bedrooms = *float*(st.selectbox('Number of Bedroom',*sorted*(df['bedRoom'].unique().tolist())))                                                                                     |
|                                                                                                                                                                                     |
| bathroom = *float*(st.selectbox('Number of Bathrooms',*sorted*(df['bathroom'].unique().tolist())))                                                                                  |
|                                                                                                                                                                                     |
| balcony = st.selectbox('Balconies',*sorted*(df['balcony'].unique().tolist()))                                                                                                       |
|                                                                                                                                                                                     |
| property\_age = st.selectbox('Property Age',*sorted*(df['agePossession'].unique().tolist()))                                                                                        |
|                                                                                                                                                                                     |
| built\_up\_area = *float*(st.number\_input('Built Up Area'))                                                                                                                        |
|                                                                                                                                                                                     |
| servant\_room = *float*(st.selectbox('Servant Room',[0.0, 1.0]))                                                                                                                    |
| store\_room = *float*(st.selectbox('Store Room',[0.0, 1.0]))                                                                                                                        |
|                                                                                                                                                                                     |
| furnishing\_type = st.selectbox('Furnishing Type',*sorted*(df['furnishing\_type'].unique().tolist()))                                                                               |
| luxury\_category = st.selectbox('Luxury Category',*sorted*(df['luxury\_category'].unique().tolist()))                                                                               |
| floor\_category = st.selectbox('Floor Category',*sorted*(df['floor\_category'].unique().tolist()))                                                                                  |
|                                                                                                                                                                                     |
| *if* st.button('Predict'):                                                                                                                                                          |
|                                                                                                                                                                                     |
|     *# form a dataframe*                                                                                                                                                            |
|     data = [[property\_type, sector, bedrooms, bathroom, balcony, property\_age, built\_up\_area, servant\_room, store\_room, furnishing\_type, luxury\_category, floor\_category]] |
|     columns = ['property\_type', 'sector', 'bedRoom', 'bathroom', 'balcony',                                                                                                        |
|                'agePossession', 'built\_up\_area', 'servant room', 'store room',                                                                                                    |
|                'furnishing\_type', 'luxury\_category', 'floor\_category']                                                                                                           |
|                                                                                                                                                                                     |
|     *# Convert to DataFrame*                                                                                                                                                        |
|     one\_df = pd.DataFrame(data, columns=columns)                                                                                                                                   |
|                                                                                                                                                                                     |
|     *#st.dataframe(one\_df)*                                                                                                                                                        |
|                                                                                                                                                                                     |
|     *# predict*                                                                                                                                                                     |
|     base\_price = np.expm1(pipeline.predict(one\_df))[0]                                                                                                                            |
|     low = base\_price - 0.22                                                                                                                                                        |
|     high = base\_price + 0.22                                                                                                                                                       |
|                                                                                                                                                                                     |
|     *# display*                                                                                                                                                                     |
|     st.text("The price of the flat is between {} Cr and {} Cr".*format*(*round*(low,2),*round*(high,2)))                                                                            |
