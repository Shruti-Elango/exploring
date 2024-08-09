# NASA Image Scraper
# From archive follow each link, find image in the linked page, download the image
#Download BeautifulSoup and lxml on venv

#Download index page

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
b_url='https://apod.nasa.gov/apod/archivepix.html'
download_directory= "apod_pics"
content=urllib.request.urlopen(b_url).read()

# For each link on index page:
for link in BeautifulSoup(content, 'lxml').findAll('a'):
    print('Following this link: ', link)
    href=urljoin(b_url, link['href'])

    # Follow link and pull down the image on linked page
    new_content=urllib.request.urlopen(href).read()
    #Find image url and download from url
    for img in BeautifulSoup(new_content, 'lxml').findAll('img'):
        img_href=urljoin(href, img['src'])
        print('Downloading image: ', img_href)
        img_name = img_href.split('/')[-1]
        #downloading
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
