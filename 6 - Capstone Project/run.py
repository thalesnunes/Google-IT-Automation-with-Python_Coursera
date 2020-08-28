#!/usr/bin/env python3

import os
import requests

if __name__ == "__main__":
    
    path = os.path.expanduser('~')+'/supplier-data/descriptions'
    for file in [f for f in os.listdir(path) if '.txt' in f]:
        with open(path+'/'+file, 'r') as f:
            name, weight, descr = [x.strip() for x in f.readlines()]
            weight = int(weight.split()[0])
            fruit = {'name': name, 'weight': weight, 'description': descr, 'image_name': file.split('.')[0]+'.jpeg'}
            response = requests.post('http://104.154.28.94/fruits', json=fruit)
