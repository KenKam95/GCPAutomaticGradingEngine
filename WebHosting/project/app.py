import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu 
from helperSqlite import *
from PIL import Image

selected = option_menu(
   menu_title="Main Menu",
   options=["Student Form","Student Result"],
   icons=["envelope", "book"],
   menu_icon="cast",
   default_index=0,
   orientation="horizontal",
)

if selected == "Student Form":
   st.title("Student Form")
   Submit_form = """
   <form action="" method="POST">
         <input type="text" name="name" placeholder="Your Student email" required>
         <textarea placeholder="Type your credentials here or Upload your credentials file below"></textarea>
         <label for="file">
              upload credentials here
         </label><br>
         <input type="file" id="file">
         <button type="submit" name="submit"">Submit</button>
   </form>

   """
   st.markdown(Submit_form, unsafe_allow_html=True)

if selected == "Student Result":
     st.title("Student Result")
     excel_file = '~/project/storage/html_remarktest.xlsx'
     sheet_name = 'sheet1'
     df = pd.read_excel(excel_file)
     st.dataframe(df)

def local_css(file_name):
   with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")


