from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import requests
# import csv
# import pandas as pd
# import numpy as np

# Create your views here.
headers = {
    'accept':'*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
base_url = 'https://restoran.kz/restaurant'

def olx_photo_parse(base_url, headers):
    flats = []
    urls = []
    urls.append(base_url)
    session = requests.Session()
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        try:
            all_anchors = soup.find_all('a', attrs = {'class':'block br3 brc8 large tdnone lheight24'})
            pages = []
            
            for span in all_anchors:
                pages.extend(span.findAll('span'))
            count = int(pages[-1].text)
            for i in range(count-1):
                url = f'https://www.olx.kz/elektronika/foto-video/alma-ata/?page={i+1}'
                if url not in urls:
                    urls.append(url)
        except:
            pass
        
        for url in urls:
            request = session.get(url, headers = headers)
            soup = bs(request.content, 'lxml')
            divs = soup.find_all('div', attrs = {'class':'offer-wrapper'})
            for div in divs:
                title = div.find('strong').text
                price = div.find('p', attrs = {'class':'price'}).text
                location = div.find('i', attrs = {'data-icon':'location-filled'}).next_sibling
                image = div.find('img', attrs = {'class': 'fleft'})
                if image is None: 
                    image = None
                else:
                    image = image['src']
                flats.append({
                    'price': price,
                    'title': title,
                    'location': location,
                    'image': image
                }) 
    else:
        print('ERROR')
    return flats
                
# def files_writer(flats):
#     with open(r"Olx.csv", "w", encoding = 'utf-8') as file:
#         a_pen = csv.writer(file)
#         a_pen.writerow(('price', 'title', 'location', 'image'))
#         for flat in flats:
#             a_pen.writerow((flat['price'],flat['title'], flat['location'], flat['image']))


def parser_rest(self):
    flats = olx_photo_parse(base_url, headers)
    return HttpResponse(flats)

# files_writer(flats)