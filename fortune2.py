import requests
import re
import time
import csv
import codecs
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

with codecs.open('forbes500.csv', 'w', 'utf-8') as file_object:
	forbesWriter = csv.writer(file_object, delimiter=',', quotechar = "|", quoting = csv.QUOTE_ALL)
	forbesWriter.writerow( ['name','ceo','sector','industry','website'])
	for i in range(1, 500):
		url = urlopen('http://beta.fortune.com/fortune500/a-' + str(i))
		r = BeautifulSoup(url, "lxml")
		name = r.findAll("h1")
		ceo = r.findAll("p", {"data-reactid": re.compile("\$company-info-card-CEO\.1\.0")})
		sector = r.findAll("p", {"data-reactid": re.compile("\$company-info-card-Sector\.1\.0")})
		industry = r.findAll("p", {"data-reactid": re.compile("\$company-info-card-Industry\.1\.0")})
		website =  r.findAll("a", {"data-reactid": re.compile("\$company-info-card-Website\.1\.0")})
		rawText = r.text

		print(name[0].get_text())
		print(ceo[0].get_text())
		print(sector[0].get_text())
		print(industry[0].get_text())
		print(website[0].get_text())
		


