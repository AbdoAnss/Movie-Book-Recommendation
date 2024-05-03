# pages/data.py

import streamlit as st
import json
import pandas as pd
import os

def load_json(file_name):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, file_name)

    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def app():
    st.title("Data Page")

    # Load JSON data
    films_data = load_json('first_50_films.json')
    books_data = load_json('first_30_books.json')

    # Convert JSON data to pandas DataFrames
    films_df = pd.DataFrame(films_data['movies'])
    books_df = pd.DataFrame(books_data)

    # Convert 'Year' column to integers
    films_df['Year'] = films_df['Year'].astype(int)

    # Display data as tables
    st.subheader("First 50 Films Data")
    st.dataframe(films_df.style.set_properties(**{'text-align': 'left', 'number_format': '0f'}))

    st.subheader("First 30 Books Data")
    st.dataframe(books_df)

if __name__ == "__main__":
    app()
