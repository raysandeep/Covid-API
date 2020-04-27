import datetime
import json
import requests
import argparse
import logging
from bs4 import BeautifulSoup
from tabulate import tabulate


URL ='https://mohfw.gov.in/'
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]



def scrapper():
    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_contents(soup.tr.find_all('th'))
    stats = []
    fin = [] 
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
        if stat:
            if len(stat) == 5:
                final_stat=stat
                # print(final_stat)
                fin.append(final_stat)
    
    return fin



# print(main())