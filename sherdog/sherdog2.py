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

months = { 'Jan': 1, 'Feb' : 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

with codecs.open('sherdog.csv', 'w', 'utf-8') as file_object:
	sherdogWriter = csv.writer(file_object, delimiter=',', quotechar = "|", quoting = csv.QUOTE_ALL)
	sherdogWriter.writerow( ['name','dob,''date_of_fight','outcome'])
	for i in range(1, 5000):
		url = urlopen('http://www.sherdog/fighter/' + str(i))
		r = BeautifulSoup(url, "lxml")
		name = r.findAll("span", {"class": "fn"})
		#ceo = r.findAll("p", {"data-reactid": re.compile("\$company-info-card-CEO\.1\.0")})
		#sector = r.findAll("p", {"data-reactid": re.compile("\$company-info-card-Sector\.1\.0")})
		#industry = r.findAll("p", {"data-reactid": re.compile("\$company-info-card-Industry\.1\.0")})
		#website =  r.findAll("a", {"data-reactid": re.compile("\$company-info-card-Website\.1\.0")})
		rawText = r.text

		print(name[0].get_text())
		#print(ceo[0].get_text())
		#print(sector[0].get_text())
		#print(industry[0].get_text())
		#print(website[0].get_text())
		time.sleep(2)
		


