import requests
from bs4 import BeautifulSoup
import twitterNotify
from time import ctime,sleep

url290sqmGrey = 'http://ist.290sqm.com/adidas-originals?product_id=7954'
url290sqmBlack = 'http://ist.290sqm.com/adidas-originals?product_id=7953'

urlJordan = 'http://ist.290sqm.com/Jordan-Brand'

url =''

r = requests.get(url290sqmGrey)
soup = BeautifulSoup(r.content, "html.parser")

for value in soup.findAll('table', {'class': 'table'}):
    #print value.text
    # print type('0.00TL')
    # print type(value.text.encode('ascii','ignore'))
    # print value.text.encode('ascii','ignore').replace(" ", "")
    #print type(value.contents[1].contents[1].text.encode('ascii','ignore'))

    while 'Coming Soon' == value.contents[5].contents[3].text.encode('ascii','ignore'):
        sleep(5)
        #print ('i slept 5 seconds')
        continue
    # while 'Coming Soon' == (value.contents[1].contents[1].text.encode('ascii','ignore')):
    #     continue

    twitterNotify.url = twitterNotify.setTweet('infant yeezy is live.   ' + url290sqmGrey + '  ' + url290sqmBlack)
    print (twitterNotify.url)
    twitterNotify.main()

# rJordan = requests.get(urlJordan)
# soupJordan = BeautifulSoup(rJordan.content, "html.parser")
#
# jordan = []
#
#
#
# for value in soupJordan.findAll('div', {'class': 'product-thumb'}):
#     dict = {'item_name': 'item_name', 'item_link': 'item_link'}
#     name= value.findAll('img',{'class': 'img-responsive'})[0].get('alt').encode('ascii','ignore')
#     dict['item_name'] = name
#     #print dict['item_name']
#     link = value.findAll('a')[0].get('href').encode('ascii','ignore')
#     dict['item_link'] = link
#     #print dict['item_link']
#     jordan.append(dict)
#
# #print jordan
#
# while True:
#     for dict in jordan:
#         if dict['item_name'].__contains__('Air Jordan 12') or dict['item_name'].__contains__('Air Jordan 11'):
#             continue
#         else:
#             if dict['item_name'].__contains__('Air Jordan 1'):
#                 twitterNotify.url = twitterNotify.setTweet(dict['item_name']+ ' is live. ' + dict['item_link'])
#                 print twitterNotify.url
#                 twitterNotify.main()
#             #print "1 is not live"




