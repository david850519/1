# -*- coding:utf-8 -*-
import sys
import urllib2
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
request = urllib2.Request("https://tw.bid.yahoo.com/booth/Y9312659391?bfe=1")
response = urllib2.urlopen(request)
html = response.read()

soup=BeautifulSoup(html,'html.parser')

for item in soup.select('.item-wrap'):
        print item.select('.item-title-link')[0].text
	print item.select('.number')[0].text
	
