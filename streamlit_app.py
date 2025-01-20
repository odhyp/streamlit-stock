import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

# App title
st.set_page_config(page_title="IDX Stock Analysis", layout="wide")
st.title("📈 Indonesian Stock Market Analysis (IDX)")

# Sidebar for inputs
st.sidebar.header("Stock Selection")
ticker = st.sidebar.text_input(
    "Enter Stock Ticker (e.g., BBCA.JK, TLKM.JK):", value="BBCA.JK"
)
start_date = st.sidebar.date_input("Start Date", value=datetime(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime.today())

# Fetch stock data
if ticker:
    stock = yf.Ticker(ticker)

    # Get company information
    with st.expander("📄 Company Information", expanded=True):
        info = stock.info
        st.write(f"**Name:** {info.get('longName', 'N/A')}")
        st.write(f"**Sector:** {info.get('sector', 'N/A')}")
        st.write(f"**Industry:** {info.get('industry', 'N/A')}")
        st.write(f"**Market Cap:** {info.get('marketCap', 'N/A'):,}")
        st.write(f"**P/E Ratio:** {info.get('trailingPE', 'N/A')}")
        st.write(f"**ROE:** {info.get('returnOnEquity', 'N/A'):.2%}")
        st.write(f"**Description:** {info.get('longBusinessSummary', 'N/A')}")

    # Fetch and display historical data
    st.subheader("📊 Historical Price Data")
    try:
        history = stock.history(start=start_date, end=end_date)
        if not history.empty:
            st.write("**Price Data:**", history.tail())

            # Plot price data
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=history.index,
                    y=history["Close"],
                    mode="lines",
                    name="Close Price",
                )
            )
            fig.update_layout(
                title=f"Closing Prices of {ticker}",
                xaxis_title="Date",
                yaxis_title="Price (IDR)",
            )
            st.plotly_chart(fig)
        else:
            st.warning("No data available for the selected date range.")
    except Exception as e:
        st.error(f"Error fetching historical data: {e}")

    # Display dividends
    st.subheader("💰 Dividends Data")
    dividends = stock.dividends
    if not dividends.empty:
        st.write("**Dividends History:**", dividends.tail())
        fig_div = go.Figure()
        fig_div.add_trace(go.Bar(x=dividends.index, y=dividends, name="Dividends"))
        fig_div.update_layout(
            title=f"Dividends of {ticker}",
            xaxis_title="Date",
            yaxis_title="Dividends (IDR)",
        )
        st.plotly_chart(fig_div)
    else:
        st.info("No dividend data available.")

else:
    st.info("Please enter a stock ticker to view its analysis.")
