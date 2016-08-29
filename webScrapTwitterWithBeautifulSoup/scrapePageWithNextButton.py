import urllib2
from bs4 import BeautifulSoup
import os
import csv

def make_soup(url):
    thePage = urllib2.Request(url)
    response = urllib2.urlopen(thePage)
    soup = BeautifulSoup(response, "html.parser")
    return soup

soup = make_soup("https://www.tripadvisor.com/Hotel_Review-g60763-d3533197-Reviews-Hyatt_Union_Square_New_York-New_York_City_New_York.html")
link = soup.find(attrs={"class":"nav next rndBtn ui_button primary taLnk"})
#print link
print (link.get("href"))