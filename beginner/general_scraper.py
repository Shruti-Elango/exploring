# General Scraper
# From archive follow each link, find image in the linked page, download the image
#Download BeautifulSoup and lxml on venv

#Download index page

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
b_url= input ("Provide URL: ")
download_directory= "Images"

#store unique set of links need to visit- following through
to_visit=set((b_url,))
visited= set()

while to_visit:
    #pick link to visit
    current_page=to_visit.pop()
    #visit link
    print('Visiting: ', current_page)
    visited.add(current_page)
    content=urllib.request.urlopen(current_page).read()
    #extract new links from page
    for link in BeautifulSoup(content, 'lxml').findAll('a'):
        absolute_link= urljoin(current_page, link['href'])
        if absolute_link not in visited:
            to_visit.add(absolute_link)
        else:
            print('Already visited: ', absolute_link)
    #download images on page
    for img in BeautifulSoup(content, 'lxml').findAll('img'):
        img_href= urljoin(current_page, img['src'])
        print(' Downloading image: ', img_href)
        img_name = img_href.split('/')[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
