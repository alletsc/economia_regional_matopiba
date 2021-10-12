import pandas as pd
df = pd.read_csv("S:\gits_stella\Python\MATOPIBA_economia_regional\MATOPIBA\MATOPIBA_economia_regional\dados\exportacao_municipio_long_lag.csv")
df.head()

df.to_excel('longlat.xlsx')