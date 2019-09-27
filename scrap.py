#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
import csv

movielinklist = []	
page = requests.get('https://www.imdb.com/list/ls005750764/?sort=list_order,asc&st_dt=&mode=detail&page=6')
soup = BeautifulSoup(page.content, 'html.parser')
whatamlookingfor = soup.find
(class_="lister list detail sub-list")
movies = whatamlookingfor.find_all(class_="lister-item mode-detail")
with open('output.csv', 'w') as file:
	collumns = ['moviename', 'cast', 'certificates']