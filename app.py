import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity

movies_dict = pickle.load(open("movies.pkl","rb"))
movies = pd.DataFrame(movies_dict)


st.title("Movie Recommender system by Sarah Effiong")

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)


similarity=pickle.load(open("similarity.pkl","rb"))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]].title)           
    return recommended_movies

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie_name)

    for i in recommendations:
       st.write(i) 

