import requests
import re
import time
import csv
import codecs
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

months = { 'Jan': 1, 'Feb' : 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

with codecs.open('sherdog500.csv', 'w', 'utf-8') as file_object:
	sherdogWriter = csv.writer(file_object, delimiter=',', quotechar = "|", quoting = csv.QUOTE_ALL)
	sherdogWriter.writerow( ['name','dob,''date_of_fight','outcome'])
	for i in range(1, 5000):
		url = 'http://www.sherdog/fighter/' + str(i)
		print(url)
		theUrl = urllib.request.urlopen(url)
		#r = requests.get(url)
		r = BeautifulSoup(theUrl, "lxml")
		name = r.findAll("span", {"class": "fn"})		
		#nameCheckString = '\<span class="fn"\>(.+?)<\/span\>'
		#ceoCheckString = '\$company-info-card-CEO\.1\.0"\>(.*?)<\/p\>'
		#sectorCheckString = '\$company-info-card-Sector\.1\.0"\>(.*?)<\/p\>'
		#industryCheckString = '\$company-info-card-Industry\.1\.0"\>(.*?)<\/p\>'
		#websiteCheckString = '\$company-info-card-Website\.1\.0"\>(.*?)<\/a\>'
		rawText = r.text
		#name = re.search(nameCheckString, rawText)
		#ceo = re.search(ceoCheckString, rawText)
		#sector = re.search(sectorCheckString, rawText)
		#industry = re.search(industryCheckString, rawText)
		#website = re.search(websiteCheckString, rawText)
		#utfName = strip_non_ascii(name.group(1)).lstrip().rstrip()
		#utfCeo = strip_non_ascii(ceo.group(1)).lstrip().rstrip()
		#utfSector = strip_non_ascii(sector.group(1)).lstrip().rstrip()
		#utfIndustry = strip_non_ascii(industry.group(1)).lstrip().rstrip()
		#utfWebsite = strip_non_ascii(website.group(1)).lstrip().rstrip()
		
		#row = '"' + name.group(1) + '","' + ceo.group(1) + '","' + sector.group(1) + '","' + industry.group(1) + '","' + website.group(1) + '"\n'
		#csvRow = [utfName, utfDOB, utfDOF, utfOutcome]
		#sherdogWriter.writerow( csvRow )
		#print(name[0].get_text())
		print(rawText)
		#rowQuoted = row.replace('"','\\"')
		#file_object.write(rowQuoted)
		time.sleep(2)


