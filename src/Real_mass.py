import os 
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import pprint
from mass_numbers import do_mass_numbers

output_path = os.path.join(os.path.dirname('__file__'), '..', ) + '/output/'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def search_and_extract(file_name, search_term,  API_key, CSE_id):
    #Doing the google
    results = google_search(search_term, API_key, CSE_id, num=10)
    base_link_list = []
    for c, result in enumerate(results):
        base_link_list.append(result['link'])
        do_mass_numbers(base_url=result['link'], file_name=file_name)
        print('DONE WITH {}/{}, base url with title: {}'.format(c, len(results), result['htmlTitle']))
    print('DOOOOONE')
