#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

def check_disk_usage():
    du = shutil.disk_usage('/')
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_memory():
    mem = psutil.virtual_memory()
    return mem.available / (1024**2) > 500

if __name__ == "__main__":
    
    erro = -1
    subjects = ['Error - CPU usage is over 80%',
                'Error - Available disk space is less than 20%',
                'Error - Available memory is less than 500MB',
                'Error - localhost cannot be resolved to 127.0.0.1']
    if not check_cpu_usage():
        erro = 0
    elif not check_disk_usage():
        erro = 1
    elif not check_memory():
        erro = 2
    elif not check_localhost():
        erro = 3
    message = emails.generate_email('automation@example.com',
                                    'student-00-8b884215a588@example.com',
                                    subjects[erro],
                                    'Please check your system and resolve the issue as soon as possible.',
                                    '')
    emails.send_email(message)
