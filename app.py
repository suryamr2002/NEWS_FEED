
import pandas as pd
import requests
import spacy
import streamlit as st
import os

from spacy import displacy
from bs4 import BeautifulSoup
import yfinance as yf

st.title('Buzzing Stocks :zap:')

## get data from RSS feed
def extract_text_from_rss(rss_link):
    """
    Parses the XML and extracts the headings from the 
    links in a python list.

    """
    headings = []
    r1 = requests.get('https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms')
    r2 = requests.get(rss_link)
    soup1 = BeautifulSoup(r1.content, features='lxml')
    soup2 = BeautifulSoup(r2.content, features='lxml')
    headings1 = soup1.findAll('title')
    headings2 = (soup2.findAll('title'))
    print(headings2)
    headings = headings1 + headings2
    return headings

def stock_info(headings):
    """
    Goes over each heading to find out the entities
    and link it with the nifty 500 companies data.
    Extracts the data 
    """
    token_dict = {
        'Org': [None] * len(headings),
        'Symbol': [None] * len(headings),
        'currentPrice': [None] * len(headings),
        'dayHigh': [None] * len(headings),
        'dayLow': [None] * len(headings),
        'forwardPE': [None] * len(headings),
        'dividendYield': [None] * len(headings)
    }
    nlp = spacy.load("en_core_web_sm")
    stocks_df = pd.read_csv("./data/ind_nifty500list.csv")
    for i, title in enumerate(headings):
        doc = nlp(title.text)
        for token in doc.ents:
            try:
                if stocks_df['Company Name'].str.contains(token.text).sum():
                    symbol = stocks_df[stocks_df['Company Name'].\
                                        str.contains(token.text)]['Symbol'].values[0]
                    org_name = stocks_df[stocks_df['Company Name'].\
                                        str.contains(token.text)]['Company Name'].values[0]
                    token_dict['Org'][i] = org_name
                    token_dict['Symbol'][i] = symbol
                    stock_info = yf.Ticker(symbol+".NS").info
                    token_dict['currentPrice'][i] = stock_info['currentPrice']
                    token_dict['dayHigh'][i] = stock_info['dayHigh']
                    token_dict['dayLow'][i] = stock_info['dayLow']
                    token_dict['forwardPE'][i] = stock_info['forwardPE']
                    token_dict['dividendYield'][i] = stock_info['dividendYield']
                else:
                    pass
            except:
                pass
    output_df = pd.DataFrame(token_dict)
    return output_df



## add an input field to pass the RSS link
user_input = st.text_input("Add your RSS link here!", "https://www.moneycontrol.com/rss/buzzingstocks.xml")

## get the financial  headings
fin_headings = extract_text_from_rss(user_input)

## output the financial info through a dataframe 
output_df = stock_info(fin_headings)
output_df.drop_duplicates(inplace=True)
st.dataframe(output_df)

## display the news in an expander section
with st.expander("Expand for Financial News!"):
    for h in fin_headings:
        st.markdown("* " + h.text)
