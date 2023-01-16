import requests
import time

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f'{url} is up and running')
    except requests.exceptions.RequestException as e:
        print(f'{url} is down. Error: {e}')

while True:
    check_website('http://example.com')
    time.sleep(10800) # wait for 3 hours (3*60*60 seconds)

    
'''
$ crontab -e
0 */3 * * * /usr/bin/python3 /path/to/script.py
'''
