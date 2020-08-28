#!/usr/bin/env python3

import os
from datetime import datetime
import reports
import emails

if __name__ == "__main__":

    fulllist = []
    path = os.path.expanduser('~')+'/supplier-data/descriptions'
    for file in [f for f in os.listdir(path) if '.txt' in f]:
        with open(path+'/'+file, 'r') as f:
            name, weight, _ = [x.strip() for x in f.readlines()]
            weight = int(weight.split()[0])
            fulllist.append({'name': name, 'weight': weight})
    final_string = ''
    for item in fulllist:
        final_string += 'name: {}<br/>weight: {} lbs<br/><br/>'.format(item['name'], item['weight'])
    reports.generate_report('/tmp/processed.pdf', 'Processed Update on {}'.format(datetime.today().strftime('%Y-%m-%d')), final_string)
    message = emails.generate_email('automation@example.com',
                          'student-00-8b884215a588@example.com',
                          'Upload Completed - Online Fruit Store',
                          'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
                          '/tmp/processed.pdf')
    emails.send_email(message)
