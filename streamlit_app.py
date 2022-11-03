
import streamlit
import pandas pd



streamlit.title("My Parents Healthy Diner")
streamlit.header(' 🥣 🥗 🐔 Breakfast Menu 🥑🍞')
streamlit.text('Oats 🥣')
streamlit.text('Kale 🥗 ')
streamlit.text('Chicken 🐔')
streamlit.text('Avo and Toast 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruit_list)
