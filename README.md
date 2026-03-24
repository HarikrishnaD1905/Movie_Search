# Movie Search App

A simple Streamlit web app to search movies using the OMDb API and display details in a clean layout.

## Project Overview

- Main app: `movie_search.py`
- Framework: **Streamlit**
- HTTP client: **requests**
- Env loader: **python-dotenv**
- API used: **OMDb API** (`https://www.omdbapi.com/`)

## Requirements

Install dependencies:

```bash
pip install streamlit requests python-dotenv
```

## Setup

1. Create `.env` in project root:
   ```
   OMDB_API_KEY=your_api_key_here
   ```
2. Get the API key from: https://www.omdbapi.com/apikey.aspx

## Run

From project root:

```bash
streamlit run movie_search.py
```

## What it does

- Input movie name
- Calls OMDb API:
  - `https://www.omdbapi.com/?t=<movie>&apikey=<key>&plot=full`
- Displays:
  - Poster (if available)
  - Title, Year, Rated, Runtime, Language, Released, Country, Genre, Seasons
  - Director, Writer, Actors
  - Plot, Awards
  - Ratings (IMDb, Rotten Tomatoes, Metacritic, etc.)

## Reset search

- "🔍 Search Another Movie" button clears state and resets input.

## Notes

- If a movie is not found or API returns error, it shows a friendly error message.
- The app requires a valid OMDb API key to work.
