import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload, vector,keplergl, Sentinel1, Sentinel1_uk # import your app modules here
import datetime

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = {
    "home": {"title": "Home", "icon": "house"},
    # "heatmap": {"title": "Heatmap", "icon": "map"},
    # "upload": {"title": "Upload", "icon": "cloud-upload"},
    # "vector": {"title": "vector", "icon": "bounding-box"},
    "keplergl": {"title": "keplergl", "icon": "bounding-box"},
    "Sentinel1": {"title": "Sentinel 1", "icon": "map"},
    "Sentinel1_uk": {"title": "Sentinel 1 UK ", "icon": "map"},
    
}

titles = [app["title"] for app in apps.values()]
icons = [app["icon"] for app in apps.values()]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )
    
    
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://share.streamlit.io/giswqs/streamlit-template) is created from template that is maintained by [Qiusheng Wu](https://wetlands.io).
            [GitHub](https://github.com/giswqs)
        
        Source code: <https://github.com/giswqs/streamlit-template>

    """
    )

for app in apps:
    if apps[app]["title"] == selected:
        eval(f"{app}.app()")
        break
