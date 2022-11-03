
import streamlit
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Parents Healthy Diner")
streamlit.header(' 🥣 🥗 🐔 Breakfast Menu 🥑🍞')
streamlit.text('Oats 🥣')
streamlit.text('Kale 🥗 ')
streamlit.text('Chicken 🐔')
streamlit.text('Avo and Toast 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)


# Display the table on the page.
