import streamlit as st

# SETTING UP ROUTES & PAGES
about_page = st.Page(
    page="views/about.py",
    title="About Me | Megh",
    icon=":material/account_circle:",
    default=True,
)

project_page_1 = st.Page(
    page="views/food.py",
    title="Food Analyzer | Megh",
    icon=":material/fastfood:",
)

project_page_2 = st.Page(
    page="views/chatbot.py",
    title="Chatbot | Megh",
    icon=":material/android:",
)

# SETTING LOGO AND ICONS
st.logo("assets/logo.png")
st.sidebar.text("Made with 💝 by Megh")

# SET NAVIGATION ACTION
pg = st.navigation(
    {
        "Info": [about_page],
        "Quick Access": [project_page_1, project_page_2],
    }
)
pg.run()
