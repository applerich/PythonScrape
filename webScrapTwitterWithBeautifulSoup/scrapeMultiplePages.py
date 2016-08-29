import urllib2
from bs4 import BeautifulSoup
import os
import csv
from string import ascii_lowercase

def make_soup(url):
    thePage = urllib2.Request(url)
    response = urllib2.urlopen(thePage)
    soup = BeautifulSoup(response, "html.parser")
    return soup

playsaved = []
for letter in ascii_lowercase:
    tablePage = make_soup("http://www.basketball-reference.com/players/" + letter+"/")
    for record in tablePage.findAll('tr'):
        playerdata = []
        for data in record.findAll('td'):
            playerdata.append(data.text)  # print (data.text)
        # print playerdata
        playsaved.append(playerdata)


header = ["Player","From","To","Pos","Ht","Wt","Birth Date","College"]# + "\n"



csvfile = file('AllBasketballPlayersWithWriterows.csv', 'wb')
writer = csv.writer(csvfile)#writing array is working fine
writer.writerow(header)
writer.writerows(playsaved) #same result as above



