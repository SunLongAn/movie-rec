import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['clean_title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].clean_title)

    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Please select a movie you enjoy:',
    movies['clean_title'])

if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie_name)
    st.write("Based on your selection, we recommend the following movies:")
    for j in recommendations:
        st.write(j)
