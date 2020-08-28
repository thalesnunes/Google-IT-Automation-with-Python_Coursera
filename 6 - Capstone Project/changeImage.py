#!/usr/bin/env python3

from PIL import Image
import os

if __name__ == "__main__":
    
    oldpath = os.path.expanduser('~')+'/supplier-data/images'
    for file in [f for f in os.listdir(oldpath) if '.tiff' in f]:
        img = Image.open(oldpath+'/'+file)
        img.resize((600,400)).convert('RGB').save(oldpath+file.split('.')[0], 'jpeg')
        