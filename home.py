import streamlit as st
import pandas as pd
import geopandas as gpd
import random

import folium
from folium.plugins import Draw, Fullscreen, LocateControl, GroupedLayerControl
from streamlit_folium import st_folium
import datetime
from datetime import datetime, timedelta, date
import random

import ast

from supabase import create_client, Client


from streamlit_cookies_controller import CookieController
import time

st.set_page_config(
    initial_sidebar_state="collapsed",
    layout="wide",
    page_title="My space",
    
)

def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()
rows_users = supabase.table("df_users").select("*").execute()
df_references = pd.DataFrame(rows_users.data)


controller = CookieController()




#---APP---
page_1 = st.Page("page/yes.py", title="Navigatie",icon=":material/explore:" )
page_2 = st.Page("page/yes_2.py", title="Navigatie",icon=":material/explore:" )



#---APP---
# IMAGE = "image/logo.png"
# IMAGE_2 ="image/menu.jpg"
# st.logo(IMAGE,  link=None, size="large",icon_image=IMAGE)


pg = st.navigation([page_1,page_2],position="sidebar",)



pg.run()
