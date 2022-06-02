import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header ('breakfast menus')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinich & Rocket Smoothoe')
streamlit.text ('🥚🐔Hard-bolied Free-Range Egg')
steamlit.text('🥑🥑Avacado Toast')  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
