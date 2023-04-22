# NEWS_FEED
# Buzzing Stocks 📈💹💰

This is a simple app that fetches financial news from an RSS feed and extracts the stock information from the news headings. It then looks up the stock information for the Nifty 500 companies and displays it in a table.

## Requirements

This app requires the following packages to be installed:

- pandas
- requests
- spacy
- pip install -U pip setuptools wheel
- streamlit
- beautifulsoup4
- yfinance

You can install these packages by running:

```bash
$ pip install pandas
requests
spacy
streamlit
beautifulsoup4
yfinance
pip
setuptools
wheel

[spacy]
spacy==3.2.0
en_core_web_sm==3.1.0

```
Usage
To run the app, use the following command:
``` bash
streamlit run app.py
```
The app will open in your web browser.

>>>>>>>>
How it Works 🔍📰📊
The app extracts the financial news from an RSS feed and looks for stock information in the news headings. It then searches the Nifty 500 companies list to find the stock symbol and other information for the company mentioned in the news heading. Finally, it displays the stock information for all the companies mentioned in the news headings in a table.

Acknowledgements 💻🌟🎉
This app was created using the following resources:

- [Streamlit](https://streamlit.io/)
- [spaCy](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Yahoo Finance API](https://finance.yahoo.com/)
- [Nifty 500 Companies List](https://www1.nseindia.com/content/indices/ind_nifty500list.csv) <br>

Author  📌👨‍💻
-> This app was created by [surya2002mr](https://github.com/suryamr2002).

