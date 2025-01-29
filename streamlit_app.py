"""
A Streamlit app for IDX Stock Analysis
Built using Streamlit, requests, and BeautifulSoup
By: Odhy Pradhana (odhyp.com) - MIT LICENSE
"""

import streamlit as st

from src.data_scraper import scrape_yahoo_finance


class StreamlitApp:
    """
    A class-based Streamlit application for IDX Stock Analysis.

    This app includes four main pages:
    1. Introduction
    2. Overview
    3. Fundamental Analysis
    4. Technical Analysis

    The app fetches stock data using `requests` and `BeautifulSoup` and displays
    the analysis interactively.
    """

    def __init__(self):
        """
        Initializes the Streamlit application by setting up the page and session state.
        """
        self.setup_page()
        self.initialize_session_state()

    def setup_page(self):
        """
        Configures the Streamlit page settings, including title, icon, and layout.
        """
        st.set_page_config(
            page_title="IDX Stock Analysis by Odai",
            page_icon="😎",
            layout="wide",
            initial_sidebar_state="expanded",
        )

    def initialize_session_state(self):
        """
        Initializes session state variables to maintain the selected page across reruns.
        """
        if "page" not in st.session_state:
            st.session_state.page = "Introduction"

    def sidebar_navigation(self):
        """
        Creates the sidebar navigation menu with buttons for different pages.
        """
        st.sidebar.header("IDX Stock Analysis")
        st.sidebar.caption(
            "🚀 A lightweight stock analysis app that scrapes and evaluates IDX stock financial data for better investment plan."
        )

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
        """
        Renders the selected page content dynamically based on session state.
        """
        if st.session_state.page == "Introduction":
            self.page_introduction()

        elif st.session_state.page == "Overview":
            self.page_overview()

        elif st.session_state.page == "Fundamental":
            self.page_fundamental()

        elif st.session_state.page == "Technical":
            self.page_technical()

    def page_introduction(self):
        """
        Displays the Introduction page.
        """
        st.title("👋 Welcome!")
        st.write("This is the welcome page of this project")

    def page_overview(self):
        """
        Displays the Overview page.
        """
        st.title("📖 Stock Overview")

        a1, a2 = st.columns(2)
        a1.write(
            "This page provides a bird’s-eye view of an IDX-listed company, displaying key details such as its name, description, sector, industry, and essential financial information"
        )

        ticker = st.text_input(
            "Enter IDX stock:", placeholder="e.g. BBCA or ADRO", max_chars=4
        ).upper()

        if ticker:
            stock_data = scrape_yahoo_finance(ticker)

            if stock_data:
                col1, col2 = st.columns([5, 2], gap="large")

                # Company name
                col1.subheader("Name:")
                col1.write(stock_data["name"])

                # Company desc
                col1.subheader("Description:")
                col1.write(stock_data["description"])

                # Company sector
                col2.subheader("Sector:")
                col2.write(stock_data["sector"])

                # Company industry
                col2.subheader("Industry:")
                col2.write(stock_data["industry"])
            else:
                st.error(
                    "Failed to retrieve stock data. Please check the ticker and try again."
                )
        else:
            st.info("Please enter a stock ticker to fetch data!")

    def page_fundamental(self):
        """
        Displays the Fundamental Analysis page.
        """
        st.title("📊 Fundamental Analysis")
        st.info("Coming soon!")

    def page_technical(self):
        """
        Displays the Technical Analysis page.
        """
        st.title("📈 Technical Analysis")
        st.info("Coming soon!")

    def run(self):
        """
        Runs the Streamlit application by handling navigation and rendering pages.
        """
        self.sidebar_navigation()
        self.render_page()


if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
