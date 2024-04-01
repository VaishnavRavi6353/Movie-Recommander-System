import streamlit as st
import pickle
import pandas

def recommend(movie):
    recommend_movies = []
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similiraty[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse = True, key=lambda x:x[1])[1:11]

    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

st.title("Movie Recommender System")

movies = pickle.load(open("movies.pkl", 'rb'))
similiraty = pickle.load(open('similiraty.pkl','rb'))


movie = st.selectbox("Select Movie:", movies['title'].values)

button = st.button("Recommend")

if button:
    recommended_movies = recommend(movie)
    count = 1
    for i in recommended_movies:
        st.write(f"{count}. {i}")
        count+=1