#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# get the url from the command line arguments use argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('url', help='url to pdf-fy')
args = parser.parse_args()

# making requests instance
reqs = requests.get(args.url)
 
# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')
 
# # displaying the title
# print("Title of the website is : ")
# for title in soup.find_all('title'):
#     print(title.get_text())

# from wkhtmltopdf import WKHtmlToPdf
# wkhtmltopdf = WKHtmlToPdf(url=args.url,output_file=title.get_text())
# wkhtmltopdf.render()

import subprocess
import re

# if soup.find_all('title') is not empty
if soup.find_all('title'):
    # get the title of the website
    title = soup.find_all('title')[0]
    # remove the special characters from the title
    title_ascii = re.sub(r'\W+ ', ' - ', title.get_text())
    # remove the extra spaces from the title
    title_ascii = re.sub(r' +', ' ', title_ascii)
    subprocess.run(['wkhtmltopdf', args.url, title_ascii+'.pdf'])
else:
    raise Exception("No title found")
