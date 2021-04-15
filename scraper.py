import requests
from bs4 import BeautifulSoup

#PS5 URL Request
ps5Page = requests.get('https://www.nowinstock.net/videogaming/consoles/sonyps5/')
#BeautifulSoup Object Containing Website Data
ps5Soup = BeautifulSoup(ps5Page.content, 'html.parser')

#URL Inventory Body
ps5TrackerContent = ps5Soup.find(id='tracker')
ps5Stores = (ps5TrackerContent.find_all(id='data'))

#BestBuy PS5 Inventory
bbyPs5 = (ps5Soup.find(id='tr53043'))
bbyPs5Inventory = (bbyPs5.find(class_='stockStatus').get_text())

#BestBuy PS5 Digital Inventory
bbyDigitalPs5 = (ps5Soup.find(id='tr53042'))
bbyDigitalPs5Inventory = (bbyDigitalPs5.find(class_='stockStatus').get_text())

#############################################################################

#Xbox Series X URL Request
xboxPage = requests.get('https://www.nowinstock.net/videogaming/consoles/microsoftxboxseriesx/')
#BeautifulSoup Object
xboxSoup = BeautifulSoup(xboxPage.content, 'html.parser')

#URL Body
xboxTrackerContent = xboxSoup.find(id='tracker')
xboxStores = (xboxTrackerContent.find_all(id='data'))

#BestBuy Xbox Series X Inventory
bbyXbox = (xboxSoup.find(id='tr53155'))
bbyXboxInventory = (bbyXbox.find(class_='stockStatus').get_text())

#############################################################################

#Function For Stock Availability
ps5Unavailable = 'Out of Stock'
ps5DigitalUnavailable = 'Out of Stock'
xboxUnavailable = 'Out of Stock'

def ps5Availability():
    if bool(bbyPs5Inventory == ps5Unavailable):
        print('BestBuy - PS5 Inventory: Out Of Stock...')
        return False
    else:
        print('BestBuy - PS5 Inventory: IN STOCK!!!')
        return True

def ps5DigitalAvailability():
    if bool(bbyDigitalPs5Inventory == ps5DigitalUnavailable):
        print('BestBuy - PS5 Digital Inventory: Out Of Stock...')
        return False
    else:
        print('BestBuy - PS5 Digital Inventory: IN STOCK!!!')
        return True

def xboxAvailability():
    if bool(bbyXboxInventory == xboxUnavailable):
        print('BestBuy - Xbox Series X Inventory: Out Of Stock...')
        return False
    else:
        print('BestBuy - Xbox Series X Inventory: IN STOCK!!!')
        return True

print('***********************************************************')
ps5Availability()
ps5DigitalAvailability()
print('-----------------------------------------------------------')
xboxAvailability()
print('***********************************************************')

