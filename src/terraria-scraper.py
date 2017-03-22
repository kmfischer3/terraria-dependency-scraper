#!/usr/bin/env python3

import urllib.request
from urllib.request import Request, urlopen
import bs4

# create the soup from url
req = urllib.request.Request('https://terraria.gamepedia.com/Crafting_station', headers={'User-Agent': 'Mozilla/5.0'})
page = bs4.BeautifulSoup(urllib.request.urlopen(req))

# extract data groups from soup
aTags = page.find_all('a')

aArr = []
for a in aTags:
	href = a.get_text()
	aArr.append(href)

print('; '.join(aArr))