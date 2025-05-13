import streamlit as st
import pickle
import pandas as pd
import requests

omdb_api =  'your_api'


def fetch_poster_omdb(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={omdb_api}"
    response = requests.get(url)
    data = response.json()
    print(f"Movie: {movie_name}, Response: {data}")
    if data.get("Poster") and data["Poster"] != "N/A":
        return data["Poster"]
    return None


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity_list[movie_index]
    my_movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in my_movies_list:
        movie_id = i[0]
        #fetch poster using movie_id form api
        recommended_movies.append(movies_list.iloc[movie_id].title)

    return recommended_movies

movies_list = pickle.load(open('movies.pkl','rb'))
similarity_list = pickle.load(open('similarity.pkl','rb'))
#movies_list = movies_list['title'].values
st.title('MOVIE RECOMMENDER SYSTEM')

mov_titles = movies_list['title'].values
selected_movie_name = st.selectbox(
'WHAT TYPE OF MOVIE WOULD YOU LIKE TO SEE ?',mov_titles
)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    poster_urls = []
    for i in names:
        poster_urls.append(fetch_poster_omdb(i))

    cols = st.columns(5)  # Create 5 side-by-side columns

    for idx, col in enumerate(cols):
        with col:
            if poster_urls[idx] :
                st.image(poster_urls[idx], use_container_width=True)
                col.markdown(
                f"<p style='text-align: center; font-size: 14px; margin-top: 5px;'>{names[idx]}</p>",
                unsafe_allow_html=True
                )
            else :
                st.write(names[idx])
                st.write("Poseter not available!!!")


    


