import requests
from bs4 import BeautifulSoup
import twitterNotify
from time import ctime,sleep


url ='http://www.adidas.com/us/yeezy'

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for value in soup.findAll('div', {'class': 'yeezy'}):
    print value.text
    # print type('0.00TL')
    # print type(value.text.encode('ascii','ignore'))
    # print value.text.encode('ascii','ignore').replace(" ", "")
    #print type(value.contents[1].contents[1].text.encode('ascii','ignore'))

    print value.contents

    # while 'Coming Soon' == value.contents[5].contents[3].text.encode('ascii','ignore'):
    #     sleep(5)
    #     #print ('i slept 5 seconds')
    #     continue




    # while 'Coming Soon' == (value.contents[1].contents[1].text.encode('ascii','ignore')):
    #     continue

    # twitterNotify.url = twitterNotify.setTweet('infant yeezy is live.   ' + url290sqmGrey + '  ' + url290sqmBlack)
    # print (twitterNotify.url)
    # twitterNotify.main()





