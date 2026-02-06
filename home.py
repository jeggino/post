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



#---APP---



page_1 = st.Page("page/web.py", title="Web",icon=":material/web:" )
page_2 = st.Page("page/areas.py", title="Gebieden",icon=":material/polygon:" )

pages = {
    "Your account": [
        page_1,

    ],
    "Resources": [
        page_2,
    ],
}

pg = st.navigation(pages, position="top")
pg.run()



