# get filename from command line with argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('urlfilelist', help='File containing list of urls to pdf-fy')
args = parser.parse_args()

# read the file containing the urls
with open(args.urlfilelist, 'r') as f:
    urls = f.readlines()

# for each url in the file
for url in urls:
    # remove the newline character from the url
    url = url.rstrip()
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
        # make a wkhtmltopdf instance
        wkhtmltopdf = WKHtmlToPdf(url=url,output_file=title_ascii+'.pdf')
        # render the pdf
        wkhtmltopdf.render()
    else:
        raise Exception("No title found")
