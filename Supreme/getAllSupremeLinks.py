import requests
from bs4 import BeautifulSoup

# the page u wanna crawl
URL = 'http://www.supremenewyork.com/shop/new'

supreme = 'http://www.supremenewyork.com'

r =requests.get(URL)

soup = BeautifulSoup(r.content, "html.parser")

#result = []    # to store all item detail data
dict =  {'item_name': 'item_name', 'item_color': 'item_color', 'item_description': 'item_description',
         'item_link': 'item_link'}

#test_link = 'http://www.supremenewyork.com/shop/sweatshirts/r0qwafb9z/alqwtnzos'

#get an item's name, color, and description
# .encode('ascii','ignore')  is used to convert uicode to string
def get_item_data(item_link):
    r = requests.get(item_link)
    soup = BeautifulSoup(r.content, "html.parser")
    for data in soup.findAll('h1', {'itemprop': 'name'}):
        dict['item_name'] = str(data.text.encode('ascii','ignore'))
    for data in soup.findAll('p', {'itemprop': 'model'}):
        dict['item_color'] = str(data.text)
    for data in soup.findAll('p', {'class': 'description'}):
        dict['item_description'] = str(data.text.encode('ascii','ignore'))
    dict['item_link'] = item_link
    print dict



#get_item_data(test_link)


# get all items links, then from each item link get item details
for link in soup.findAll('div', {'class': 'inner-article'}):
    temp_link = link.contents[0].get('href')
    item_link = supreme + temp_link
    item_link = str(item_link)
    get_item_data(item_link)





