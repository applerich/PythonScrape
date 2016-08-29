import urllib2
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thePage = urllib2.Request(url)
    response = urllib2.urlopen(thePage)
    soup = BeautifulSoup(response, "html.parser")
    return soup

url = "http://www.nike.com/cn/zh_cn/launch/c/2016-09/air-jordan-1-retro-high-og-banned"
soup = make_soup(url)

for img in soup.find_all("img"):
    temp = img.get('src') #print (img.get('src'))
    #print type(temp)
    #del some hyper links
    if temp is not None: # temp == None   temp is None will not be working
        if temp[:1] == "/":
            image = url + temp
        else:
            image = temp

        #print image

    i = 1
    nametemp = img.get('alt')
    if nametemp is not None:
        if len(nametemp) == 0:
            filename = str(i)
            i = i + 1
        else:
            filename = nametemp
        #print filename
        #if filename[:1] == 'A':
            #print filename
        try:
            imagefile = open("/home/zhiboliu/Pictures/Nike/AirJordan1/"+filename + ".jpeg", "wb")
            #print img
            image1 = urllib2.urlopen(image).read()
            imagefile.write(image1)
            print (filename + " is downloaded successfully.")
            imagefile.close()
        except IOError:
            print filename +" is broken."

