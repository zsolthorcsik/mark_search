import os 
import requests
from bs4 import BeautifulSoup
from Get_Numbers import NumberCollector
from urllib.parse import urlparse

'''
This file uses the Get_Numbers to collect the numbered sentences.
What it does is that it goes on the base_url and looks for all the <a> tags (first layer links) and collects numbered sentences there as well.
'''
def do_mass_numbers(base_url, file_name):
    base_base = urlparse(base_url)[1]

    response = requests.get(base_url, timeout = 10)
    html = response.content
    response.close()
    soup = BeautifulSoup(html, 'lxml')

    link_list = []
    link_list.append(base_url)
    for tag in soup.findAll('a'):
        try:
            if tag.get('href')[-3:] != 'pdf':
                link_list.append(tag.get('href'))
        except:
            pass

    done_links = []
    for c, link in enumerate(link_list):
        if link not in done_links:
            try: 
                NumberCollector.numbered_sentences(url=link, file_name=file_name)
            except:
                try:
                    link = 'http://' + base_base + link
                except:
                    pass
        else:
            print('Already done')
        done_links.append(link)
        print('{}/{} done'.format(c, len(link_list)))
