import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.bestbuy.com/'

#IP Mask
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
}

#Requests for URL data
r = requests.get('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')
soup = BeautifulSoup(r.content, 'lxml')

#Adding item name to ps5List
ps5List = soup.find_all('div', class_ = 'shop-product-title')

print(ps5List)



