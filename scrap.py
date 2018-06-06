
# coding: utf-8
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
import csv

# URL of page to be scraped
data_url = "http://edu.sina.com.cn/gaokao/baoming/"
data = pd.read_html(data_url)


# Create DataFrame
df = data[0]
df.columns = ["Province", '2017', '2016', '2015', '2014', '2013', '2012', '2011']
df = df.drop([0, 1])


# Remove unwanted symbols
for column in df.columns:
    df[column] = df[column].map(lambda x: x.lstrip('约超近').rstrip("↑↓+万万余"))


# Reset the index to make sure it starts from 0
df = df.reset_index(drop=True)

# Save data as csv file
df.to_csv("Data/gaokao_population.csv")
