#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    app.run(debug=True)
