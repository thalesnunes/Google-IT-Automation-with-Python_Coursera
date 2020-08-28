#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
path = os.path.expanduser('~')+'/supplier-data/images'
for file in [f for f in os.listdir(path) if '.jpeg' in f]:
    with open(path+'/'+file, 'rb') as current:
        r = requests.post(url, files={'file': current})
