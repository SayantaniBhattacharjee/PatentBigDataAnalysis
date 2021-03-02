from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging
import urllib.request

grant_list = []
application_list=[]

def crawling_data_from_reedtech():
    reedtech_grant_fulltext_url = "http://patents.reedtech.com/pgrbft.php"
    reedtech_application_fulltext_url = "http://patents.reedtech.com/parbft.php"
    grant_page = urlopen(reedtech_grant_fulltext_url)
    application_page = urlopen(reedtech_application_fulltext_url)
    soup_grant = BeautifulSoup(grant_page.read(), 'html.parser')
    soup_application = BeautifulSoup(application_page.read(), 'html.parser')
    logging.info('start to crawl grant')

    for patent_link in soup_grant.findAll('a'):
        if patent_link['href'].endswith('.zip'):
            grant_list.append("http://patents.reedtech.com/" + patent_link['href'])
    print(grant_list)

    logging.info('start to crawl application')

    for patent_link in soup_application.findAll('a'):
        if patent_link['href'].endswith('.zip'):
            application_list.append("http://patents.reedtech.com/" + patent_link['href'])

    for link in application_list:
        print (link + "\n")



def get_filename_from_patent_url(patent_url):
    return patent_url.split("/")[-1]


def download_data(patent_url):
    logging.info('Starting Downlaod : '+ patent_url)
    filename = get_filename_from_patent_url(patent_url)
    try:
        fname, header = urllib.request.urlretrieve(patent_url, filename)
    except urllib.error.HTTPError as e:
        logging.error("Connection refused: " + e)
    else:
        logging.info('Download Finished')
        logging.info(fname + ' created')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    crawling_data_from_reedtech()
    logging.info("Starting Download of Grant Patents")
    for link in grant_list:
        download_data(link)
    logging.info("Starting Download of Application Patents")
    for link in application_list:
        download_data(link)




