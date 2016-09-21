#!/usr/bin/env python
#Author SOLEHEATONFEET

import json
import requests

#Replace with your pid
pid = "B42410"

session=requests.Session()

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

#client unknown
#prodInfoUrl="http://dw-us.adidas.com/s/adidas-US/dw/shop/v15_6/products/"+pid+"?client_id=619c7dba-cadc-4c2f-8033-db6bbfe07742&expand=availability,variations,prices"

prodInfoUrl="http://dw-us.adidas.com/s/adidas-US/dw/shop/v15_6/products/"+pid+"?client_id=d958ef63-4644-4a9d-9007-03cf30262f61&expand=availability,variations,prices"

# http://production-us-adidasgroup.demandware.net/s/adidas-US/dw/shop/v15_6/products/C77124?client_id=d958ef63-4644-4a9d-9007-03cf30262f61&expand=availability,variations,prices

#You can loop the process and get updated stock
r=session.get(prodInfoUrl, headers=headers)
dictionary=json.loads(r.text)
print dictionary
print dictionary["name"]+" Stock Levels - Total Pairs: "+str(dictionary["inventory"]["ats"])

for s in dictionary["variants"]:
    if s["orderable"]:
        resp=session.get(s["link"]+"&expand=availability", headers=headers)
        l=json.loads(resp.text)
        sizespace=5-len(l["c_sizeSearchValue"])
        stockspace=5-len(str(l["inventory"]["stock_level"]))
        print "Size "+l["c_sizeSearchValue"]+" "*sizespace+" : "+str(l["inventory"]["stock_level"])+" "*stockspace+" : "+l["id"]