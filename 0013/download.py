#! /usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

def getImagesUrlFromUrl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    imgs = soup.find_all('img')
    urls = []
    for tag in imgs:
       try:
           if 'BDE_Image' in tag['class']:
               print(tag['src'])
               urls.append(tag['src'])
           else:
               imgs.remove(tag)
       except Exception as e:
           imgs.remove(tag)
    return urls

def downImgFromUrls(urls):
    for url in urls:
        r = requests.get(url, stream=True)
        o = urlparse(url)
        filename = os.path.basename(o.path)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

if __name__ == "__main__":
    imgs = getImagesUrlFromUrl('http://tieba.baidu.com/p/2166231880')
    downImgFromUrls(imgs)
    #  r = requests.get('http://tieba.baidu.com/p/2166231880')
    #  soup = BeautifulSoup(r.text, "html.parser")
    #  imgs = soup.find_all('img')
    #  for tag in imgs:
    #     try:
    #         if 'BDE_Image' in tag['class']:
    #             print(tag['src'])
    #     except Exception as e:
    #         pass
         

