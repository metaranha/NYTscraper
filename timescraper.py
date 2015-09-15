#!/usr/bin/python
#New York Times Bestseller list scraper (/u/metaranha <3)

import urllib
from bs4 import BeautifulSoup

#pulls HTML for the site
htmlfile = urllib.urlopen("http://www.nytimes.com/best-sellers-books/")
htmltext = htmlfile.read()

#opens new file for dropping all of the HTML from the site
f=open('out.txt', 'w')
print >> f, htmltext
f.close()

#creates beautifulsoup objects
soup = BeautifulSoup(htmltext)

#finds all 'li' instances; assigns variable
findli = soup.find_all("li")

#opens a new text file and prints all of the <li> instances
f=open('li.txt', 'w')
print >> f, findli
f.close()

#searches all <li> instances for instances of <b> tag
for line in soup.find_all("b"):
#prints each instance neatly to the terminal
    print line.text
