import streamlit as st
import streamlit.components.v1 as components

import streamlit.components.v1 as components

components.iframe("https://www.elskenecologie.nl/contact-elsken-ecologie-nh-terschelling/")



# Read the HTML file
with open('files/BUCK_TK_Fietsroutes.html', 'r') as file:
    html_content = file.read()

# Render the HTML
components.html(html_content, height=600)



