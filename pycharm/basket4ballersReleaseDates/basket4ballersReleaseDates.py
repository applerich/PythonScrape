# release calendar for http://www.basket4ballers.com/en/

import requests
from bs4 import BeautifulSoup

URL = 'http://blog.basket4ballers.com/fr/release-date'

r = requests.get(URL)

soup = BeautifulSoup(r.content,"html.parser")

for item in soup.findAll('div',{'class':'views-row'}):
    print item.findAll('h2',{'class':'node__title flush--right node__title--large'})[0].text #item name
    print item.findAll('p')[0].text #color
    print item.findAll('p')[1].text  # Style code
    print item.findAll('p')[2].text  # Price
    print 'Release time: '+item.findAll('time')[0].text  #time
    print 'Buy it here: '+item.findAll('a',{'class':'share__link share__link--grey img__ico-addtocart'})[0].get('href') #buy link
