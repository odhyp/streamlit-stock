import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_yahoo_finance(ticker: str):
    idx_ticker = f"{ticker}.JK"

    base_url = f"https://finance.yahoo.com/quote/"
    profile_url = f"{base_url}{idx_ticker}/profile"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    response = requests.get(profile_url, headers=headers, timeout=30)

    if response.status_code != 200:
        print(f"Failed to fetch data for {ticker}: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    data = {}

    # PROFILE PAGE
    try:
        # Company name
        company_name = soup.select("section.container > h1")
        data["name"] = company_name[0].text

        # Company description
        company_desc = soup.select("section > section > p")
        data["description"] = company_desc[0].text

        # Company stats
        company_stats = soup.select("div.company-details > dl.company-stats > div")
        company_sector = company_stats[0].find("a").text.strip()
        company_industry = company_stats[1].find("a").text.strip()
        data["sector"] = company_sector
        data["industry"] = company_industry

    except AttributeError as e:
        print(f"Error scraping data for {ticker}: {e}")

    return data
