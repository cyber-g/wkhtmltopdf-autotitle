#!/usr/bin/env python3

# get filename from command line with argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('urlfilelist', help='Filename containing list of urls to pdf-fy')
args = parser.parse_args()

# read the file containing the urls
with open(args.urlfilelist, 'r') as f:
    urls = f.readlines()

import requests
from bs4 import BeautifulSoup
import re
import subprocess

# for each url in the file
for url in urls:
    # remove the newline character from the url
    url = url.rstrip()
    # if URL begins with %, ignore line
    if url.startswith('%'):
        continue
    # check that URL is valid
    elif not re.match(r'^https?://.*', url):
        raise Exception("Invalid URL")
    # Print the url
    print('Processing URL: ',url)
    # make a requests instance
    reqs = requests.get(url)
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    # if soup.find_all('title') is not empty
    if soup.find_all('title'):
        # get the title of the website
        title = soup.find_all('title')[0]
        # remove the special characters from the title
        title_ascii = re.sub(r'\W+ ', ' - ', title.get_text())
        # remove the extra spaces from the title
        title_ascii = re.sub(r' +', ' ', title_ascii)
        # call wkhtmltopdf
        subprocess.run(['wkhtmltopdf', url, title_ascii+'.pdf'])
    else:
        raise Exception("No title found")
