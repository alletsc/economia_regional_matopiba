import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

req = requests.get('https://journals.openedition.org/confins/13045')
content = req.content

soup = bs(content, 'html.parser')
table = soup.find_all(id='Table1')

table_str = str(table)

df = pd.read_html(table_str)[0]
matopiba_urban = pd.DataFrame.copy(df)

matopiba_urban = matopiba_urban.rename(columns={0: 'Estado'})
matopiba_urban = matopiba_urban.rename(columns={1: 'Municipios'})
matopiba_urban = matopiba_urban.rename(columns={2: 'População'})
matopiba_urban = matopiba_urban.rename(columns={3: 'População (%)'})
matopiba_urban = matopiba_urban.rename(columns={4: 'Território (%)'})
matopiba_urban = matopiba_urban.rename(columns={5: 'Taxa Urbanização'})

matopiba_urban = matopiba_urban.drop(0)
matopiba_urban = matopiba_urban.drop(['Municipios'], axis=1)

matopiba_urban
