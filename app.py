#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This code scraps mohfw.gov.in for COVID-19 Data

"""
import requests
import threading
from bs4 import BeautifulSoup
import json
import dateutil.parser as dparser
from flask import Flask
import re
import time
from time import sleep
from datetime import datetime
from algo import scrapper
app = Flask(__name__)

# Removed Foreign National Column
headers = {
    0: "id",
    1: "place",
    2: "confirmed",
    3: "cured",
    4: "deaths"
}
# Added Date Time matching REGEX to give better input to Fuzze Dateutil Parser
date_time_pattern = r"\d{2}.\d{2}.2020(.*)"
last_extracted_content = "welcome"
last_extracted_time = "2020-03-28 17:45:00"






@app.route('/', methods=['GET'])
def home():
    return '''<h1>COVID 19 India Data -- CC</h1>
    <h3>Source: <a href="https://mohfw.gov.in">Ministry of Health and Family Welfare, India</a></h3>'''


@app.route('/api', methods=['GET'])
def get_data():
    listi  =scrapper()
    final = []
    for i in listi:
        obj = {
            'no':i[0],
            'state':i[1],
            'active':i[2],
            'recoverd':i[3],
            'deadths':i[4]
        }
        final.append(obj)
    return json.dumps({
        'data':final
    })



if __name__ == "__main__":
    # #thread.start_new_thread(data_extract, ())
    # x.start()
    app.run(debug=True)
