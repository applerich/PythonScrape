import urllib2
#from urllib2 import Request
from bs4 import BeautifulSoup

theUrl = "https://twitter.com/zhibolau"
thePage = urllib2.Request(theUrl)
response = urllib2.urlopen(thePage)
soup = BeautifulSoup(response, "html.parser")

print (soup.title)
print (soup.title.text)

print (soup.findAll('a')) #find all a tag
#if i only want links from href, for loop is here to help

for link in soup.findAll('a'):
    print (link.get('href'))
    # print(link.text)

#find = findALl[0]
#wannt print my file introduction
print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p',{"class": "ProfileHeaderCard-bio u-dir"}))
print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p',{"class": "ProfileHeaderCard-bio u-dir"}).text)
print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text) #there is only one p tag, so not class id is required, also output same result with text func

#now i can print all my tweets
for tweets in soup.findAll('div',{"class":"content"}):
    print(tweets.find('p').text)

