import requests
from bs4 import BeautifulSoup
import twitterNotify

url290sqmGrey = 'http://ist.290sqm.com/adidas-originals?product_id=7835'
url290sqmBlack = 'http://ist.290sqm.com/adidas-originals?product_id=7834'

url =''

r = requests.get(url290sqmGrey)
soup = BeautifulSoup(r.content, "html.parser")

for value in soup.findAll('ul', {'class': 'list-unstyled margin-bottom-l'}):
    #print value.text
    # print type('0.00TL')
    # print type(value.text.encode('ascii','ignore'))
    # print value.text.encode('ascii','ignore').replace(" ", "")
    #print type(value.contents[1].contents[1].text.encode('ascii','ignore'))
    while '0.00TL' == (value.contents[1].contents[1].text.encode('ascii','ignore')):
        continue

    twitterNotify.url = twitterNotify.setTweet('infant yeezy is live.   ' + url290sqmGrey + '  ' + url290sqmBlack)
    print twitterNotify.url
    twitterNotify.main()



