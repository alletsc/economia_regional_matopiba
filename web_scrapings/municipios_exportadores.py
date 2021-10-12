url = 'https://journals.openedition.org/confins/17590'
req = requests.get(url)

content = req.content
soup = bs(content, 'html.parser')
tab = soup.find_all(id='Table1')
tab_str = str(tab)
df2 = pd.read_html(tab_str)[0]

expo = pd.DataFrame.copy(df2)

expo = expo.rename(columns={0: 'Estado'})
expo = expo.rename(columns={1: 'Municipio'})
expo = expo.rename(columns={2: 'Valor Exportação U$'})

expo = expo.drop(0)
expo.to_csv('expo_cit.csv')
