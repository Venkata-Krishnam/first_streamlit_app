
import streamlit
streamlit.title('my parents new healthy dinner')
streamlit.header('aBreak fast menu')
streamlit.text('omega & omlet & blueberry')
streamlit.text('idly sambar and Dosa')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
