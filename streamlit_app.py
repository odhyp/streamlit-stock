"""
A Streamlit app
"""

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd


import streamlit as st


class StreamlitApp:
    def __init__(self):
        self.setup_page()
        self.initialize_session_state()

    def setup_page(self):
        st.set_page_config(
            page_title="IDX Stock Analysis by Odai",
            page_icon="😎",
            layout="wide",
            initial_sidebar_state="expanded",
        )

    def initialize_session_state(self):
        if "page" not in st.session_state:
            st.session_state.page = "Introduction"

    def sidebar_navigation(self):
        st.sidebar.header("IDX Stock Analysis")
        st.sidebar.caption("Welcome to my Streamlit project!")

        st.sidebar.divider()
        st.sidebar.subheader("Menu")

        # Introduction page
        if st.sidebar.button(
            "Introduction", type="secondary", use_container_width=True, icon="👋"
        ):
            st.session_state.page = "Introduction"

        # Overview page
        if st.sidebar.button(
            "Overview", type="secondary", use_container_width=True, icon="📖"
        ):
            st.session_state.page = "Overview"

        # Fundamental page
        if st.sidebar.button(
            "Fundamental", type="secondary", use_container_width=True, icon="📊"
        ):
            st.session_state.page = "Fundamental"

        # Technical page
        if st.sidebar.button(
            "Technical", type="secondary", use_container_width=True, icon="📈"
        ):
            st.session_state.page = "Technical"

        st.sidebar.divider()
        st.sidebar.subheader("Information")
        st.sidebar.caption("Last update: 29/01/2025")
        st.sidebar.caption("Version 0.0.1")
        st.sidebar.caption("&copy; 2025 Odhy Pradhana. All Rights Reserved.")

    def render_page(self):
        if st.session_state.page == "Introduction":
            st.title("👋 Welcome!")
            st.write("This is the welcome page of this project")

        elif st.session_state.page == "Overview":
            st.title("📖 Stock Overview")
            st.info("Coming soon!")

        elif st.session_state.page == "Fundamental":
            st.title("📊 Fundamental Analysis")
            st.info("Coming soon!")

        elif st.session_state.page == "Technical":
            st.title("📈 Technical Analysis")
            st.info("Coming soon!")

    def run(self):
        self.sidebar_navigation()
        self.render_page()


if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
