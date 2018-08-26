import requests as r
from bs4 import BeautifulSoup as soup 

url = 'https://www.freestylephoto.biz/clearance?sort=price-asc&max=24&clearance=1'
data = r.get(url)

page_data = soup(data.text, 'html.parser')
soup_data = page_data.find_all('div', {'class': 'product-grid-top'})

import pandas as pd
df = pd.DataFrame()

for each in soup_data:
    each_price = each.find('span', {'class': 'price'}).text
    product_name = each.find('span', {'itemprop':'name'}).text
    
    df = df.append(pd.DataFrame({'Price': each_price, 'Product': product_name}, index = [0]), ignore_index = True)

df.to_csv('clearence_product_pricing_test_3.txt', sep='|', index = False)