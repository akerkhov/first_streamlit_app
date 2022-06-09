import streamlit

streamlit.title('My Parents New Healthy Diner')

#streamlit.header ('breakfast menus')
#streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
#streamlit.text ('🥗 Kale, Spinich & Rocket Smoothoe')
#streamlit.text ('🥚🐔Hard-bolied Free-Range Egg')
#steamlit.text('🥑🥑Avacado Toast')  
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('fruit')

# lets put a pick list here so they can pick the fruit they want to include
#fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avacado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
#streamlit.dataframe(my_to_show)

#new section to display fruityvice api responce
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json()))

#frutyvice_nomalized = pandas.json_normalize(frutyvice_response.json())
#streamlit.dataframe(fruityvice_normalized)

#steamlit.header('Frutyvice Fruit Advice!')
#fruit_choice - streamlit.test_input('What Fruit would yyou like information about?', 'Kiwi')
#streamlit.write('The user entered",fruit_choice)
                
#import requests
#fruityvice_reponse = requests.get("https://fruityvice.com/api/fruit/" = fruit_choice)
                
