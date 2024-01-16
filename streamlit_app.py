import streamlit as st
import pandas as pd
import requests

st.title('My Parents new Healthy Diner')

st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinack & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
# comment with all unique symbols used in section above: '🥣 🥗 🐔 🥑🍞'

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#read in the text data
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show, hide_index=True)

#New Section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# parse the JSON to tabulat format
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# render the dataframe we just created
st.dataframe(fruityvice_normalized)
