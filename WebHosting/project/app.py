import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu 
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
   Submit_form = """
   <form action="~/project/studentData/studentData.db">
         <input type="text" name="name" placeholder="Your Student Id" required>
         <input type="message" name="credentials" placeholder="credentials" requred>
         <button type="submit">Submit</button>
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
