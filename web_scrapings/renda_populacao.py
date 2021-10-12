import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from requests.api import request


url = "https://www.scielo.br/j/resr/a/Z3vsG5Tjc5nXDJ9CT8Ld7Sv/?lang=pt"
req = requests.get(url)
content = req.content

soup = bs(content, 'html.parser')
table = soup.find_all(id='Table1')
