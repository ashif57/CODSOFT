import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Title
st.title("🛍️ Simple Product Recommendation System")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("products.csv")

df = load_data()

# Show data
st.subheader("Product Catalog")
st.dataframe(df)

# TF-IDF vectorization on product descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def recommend(product_name, top_n=3):
    idx = df[df['name'] == product_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]  # Skip self match
    product_indices = [i[0] for i in sim_scores]
    return df.iloc[product_indices][['name', 'description', 'category']]

# User selection
st.subheader("Select a Product to Get Recommendations")

product_list = df['name'].tolist()
selected_product = st.selectbox("Choose a product:", product_list)

if st.button("Recommend"):
    st.subheader(f"Products similar to '{selected_product}':")
    recommendations = recommend(selected_product)
    st.table(recommendations)
