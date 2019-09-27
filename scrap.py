#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
import csv

movielinklist = []	
page = requests.get('https://www.imdb.com/list/ls005750764/?sort=list_order,asc&st_dt=&mode=detail&page=6')
soup = BeautifulSoup(page.content, 'html.parser')
whatamlookingfor = soup.find(class_="lister list detail sub-list")
movies = whatamlookingfor.find_all(class_="lister-item mode-detail")
with open('output.csv', 'w') as file:
	collumns = ['moviename', 'cast', 'certificates']
	writer = csv.DictWriter(file, fieldnames=collumns)
	writer.writeheader()
	for i, movie in enumerate(movies):
		link = movie.find(class_="lister-item-image ribbonize")
		movielinks = link.find('a')['href']
		moviename = link.find('img')['alt']
		movielink = 'https://www.imdb.com{}fullcredits'.format(movielinks.split('?')[0])
		certificates = 'https://www.imdb.com{}parentalguide'.format(movielinks.split('?')[0])
		movielinklist.append(movielink)
		writer.writerow({'moviename' : moviename})
		print('\n')
		print('Moviename:', i, moviename)
		print("----------------------------------------------")
		print(moviename + '\'s cast members')
		print('----------------------------------------------')
		page = requests.get(movielink)
		soup = BeautifulSoup(page.content, 'html.parser')
		castlist = soup.find(class_="cast_list")
		mylist = list(castlist.children)[3:-1]
		#for i in mylist:
		#	try:
		#		castmembers = i.find('img')['alt']
		#		writer.writerow({'cast' : castmembers})
		#		print(castmembers)
		#	except TypeError:
		#		pass
		#print('----------------------------------------------')
		#print(moviename + '\'s certificates')
		#print('----------------------------------------------')
		certpage = requests.get(certificates)
		certsoup = BeautifulSoup(certpage.content, 'html.parser')
		certificationlist = certsoup.find(id='certifications-list')
		certifications = certificationlist.find_all(class_='ipl-inline-list__item')
		#for certification in certifications:
		#	certification = (certification.get_text().replace('\n', ''))
		#	certification = re.sub(' +',' ', certification)
		#	print(certification)
		#	writer.writerow({'certificates' : certification})
		print('--------------------------------------------------------------------------------------------------------------')
		for i, certification in zip(mylist, certifications):
			certification = (certification.get_text().replace('\n', ''))
			certification = re.sub(' +',' ', certification)
			try:
				castmembers = i.find('img')['alt']
				writer.writerow({'moviename' : moviename, 'cast' : castmembers, 'certificates' : certification})
				print(moviename)
				print(castmembers)
				print(certification)
			except TypeError:
				pass
