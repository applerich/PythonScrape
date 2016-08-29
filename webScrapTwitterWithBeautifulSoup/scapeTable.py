import urllib2
from bs4 import BeautifulSoup
import os
import csv

def make_soup(url):
    thePage = urllib2.Request(url)
    response = urllib2.urlopen(thePage)
    soup = BeautifulSoup(response, "html.parser")
    return soup

tablePage = make_soup("http://www.basketball-reference.com/players/a/")
#tablePage = make_soup("https://www.google.com/finance/historical?q=NASDAQ%3AAAPL&ei=pVLDV8GoMeeIigL73YGQCg")

# for record in tablePage.findAll('tr'):
#     print(record.text)

# playsaved = ""
# for record in tablePage.findAll('tr'):
#     playerdata = ""
#     for data in record.findAll('td'):
#         playerdata = playerdata + ',' + data.text #print (data.text)
#     playsaved = playsaved +"\n"+ playerdata[1:]


#print playsaved

header = ["Player","From","To","Pos","Ht","Wt","Birth Date","College"]# + "\n"
playsaved = []
for record in tablePage.findAll('tr'):
    playerdata = []
    for data in record.findAll('td'):
        playerdata.append(data.text)  #print (data.text)
    #print playerdata
    playsaved.append(playerdata)


#python3
# file = open(os.path.expanduser("basketballPlayers.csv"),"wb")
# file.write(bytes(header, encoding="ascii", errors = 'ignore'))
# file.write(bytes(playsaved, encoding="ascii", errors = 'ignore'))

#python2

#csvfile = file('basketballPlayers.csv', 'wb')  #using the for loop below
csvfile = file('basketballPlayersWithWriterows.csv', 'wb')
writer = csv.writer(csvfile)#writing array is working fine
writer.writerow(header) #
# for data in playsaved:
#     print data
#     writer.writerow(data)

#better than above
writer.writerows(playsaved) #same result as above



