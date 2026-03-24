import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("OMDB_API_KEY")

st.set_page_config(page_title="Movie Search", layout="wide")

if "movie_data" not in st.session_state:
    st.session_state.movie_data = None

if "searched" not in st.session_state:
    st.session_state.searched = False

st.title("Search a Movie")

if not st.session_state.searched:
    with st.form(key="movie_form"):
        movie_name = st.text_input("Enter the movie name:")
        submit_button = st.form_submit_button("Search")

    if submit_button and movie_name:
        url = f"https://www.omdbapi.com/?t={movie_name}&apikey={apikey}&plot=full"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            st.session_state.movie_data = data
            st.session_state.searched = True
            st.rerun()
        else:
            st.error("Movie not found or API error")

if st.session_state.searched and st.session_state.movie_data:
    data = st.session_state.movie_data
    st.divider()

    col1, spacer, col2 = st.columns([1.5, 0.25, 2])

    with col1:
        poster_url = data.get("Poster")
        if poster_url and poster_url != "N/A":
            st.image(poster_url, width="stretch")
        else:
            st.warning("Poster not available")

    with col2:
        st.title(data.get("Title", "N/A"))

        col_a, col_b = st.columns(2)
        with col_a:
            st.write(f"**Year:** {data.get('Year', 'N/A')}")
            st.write(f"**Rated:** {data.get('Rated', 'N/A')}")
            st.write(f"**Runtime:** {data.get('Runtime', 'N/A')}")
            st.write(f"**Language:** {data.get('Language', 'N/A')}")
        with col_b:
            st.write(f"**Released:** {data.get('Released', 'N/A')}")
            st.write(f"**Country:** {data.get('Country', 'N/A')}")
            st.write(f"**Genre:** {data.get('Genre', 'N/A')}")
            st.write(f"**Seasons:** {data.get('totalSeasons', 'N/A')}")

        st.divider()

        st.write(f"**Director:** {data.get('Director', 'N/A')}")
        st.write(f"**Writer:** {data.get('Writer', 'N/A')}")
        st.write(f"**Actors:** {data.get('Actors', 'N/A')}")

        st.divider()

        st.markdown("**Plot**")
        st.write(data.get("Plot", "N/A"))

        st.divider()

        col_rating, col_awards = st.columns(2)
        with col_rating:
            if data.get("imdbRating") != "N/A":
                st.metric("IMDb Rating", data.get("imdbRating", "N/A"), "/ 10")
            else:
                st.write(f"**IMDb Rating:** {data.get('imdbRating', 'N/A')}")
        with col_awards:
            st.write(f"**Awards:** {data.get('Awards', 'N/A')}")

        if data.get("Ratings"):
            st.divider()

            for rating in data["Ratings"]:
                st.write(f"**{rating.get('Source')}:** {rating.get('Value')}")

    st.divider()
    if st.button("🔍 Search Another Movie"):
        st.session_state.searched = False
        st.session_state.movie_data = None
        st.rerun()
