from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging
import urllib.request

list_google_patent = []
list_reedtech_patent = []



def crawling_data_from_google():
    google_grant_fulltext_url = "https://www.google.com/googlebooks/uspto-patents-grants-text.html"
    google_application_fulltext_url = "https://www.google.com/googlebooks/uspto-patents-applications-text.html"
    google_grant_page = urlopen(google_grant_fulltext_url)
    google_application_page = urlopen(google_application_fulltext_url)
    soup_grant = BeautifulSoup(google_grant_page.read(), 'html.parser')
    soup_application = BeautifulSoup(google_application_page.read(), 'html.parser')
    logging.info('Start to crawl google grant till 2015')
    crawling_webpage_on_issued_date(soup_grant)
    logging.info('Start to crawl google application till 2015')
    crawling_webpage_on_issued_date(soup_application)

def crawling_webpage_on_issued_date(soup_page):
    for list in soup_page.findAll('h3') or list in soup_page.findAll('div', {'class', 'bulkyear'}):
        if list['id'] <= '2015':
            logging.info('start to crawl google patent files till 2015')
            for patent_link in soup_page.findAll('a'):
                if patent_link['href'].endswith('.zip'):
                    list_google_patent.append(patent_link['href'])
            print(list_google_patent)
        else:
            logging.info('start to crawl reedtech patent file from 2016')
            for patent_link in soup_page.findAll('a'):
                if patent_link['href'].endswith('.zip'):
                    list_reedtech_patent.append("http://patents.reedtech.com/" + patent_link['href'])
            print(list_reedtech_patent)
            

def crawling_data_from_reedtech():
    reedtech_grant_fulltext_url = "http://patents.reedtech.com/pgrbft.php"
    reedtech_application_fulltext_url = "http://patents.reedtech.com/parbft.php"
    grant_page = urlopen(reedtech_grant_fulltext_url)
    application_page = urlopen(reedtech_application_fulltext_url)
    soup_grant = BeautifulSoup(grant_page.read(), 'html.parser')
    soup_application = BeautifulSoup(application_page.read(), 'html.parser')
    logging.info('start to crawl Reedtech grant from 2016')
    crawling_webpage_on_issued_date(soup_grant)

    logging.info('start to crawl Reedtech application from 2016')
    crawling_webpage_on_issued_date(soup_application)




def get_filename_from_patent_url(patent_url):
    return patent_url.split("/")[-1]


def download_data(patent_url):
    logging.info('Starting Downlaod : ' + patent_url)
    filename = get_filename_from_patent_url(patent_url)
    try:
        fname, header = urllib.request.urlretrieve(patent_url, filename)
    except urllib.error.HTTPError as e:
        logging.error("Connection refused: " + e)
    else:
        logging.info('Download Finished')
        logging.info(fname + ' created')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    crawling_data_from_google()

    logging.info("Starting Download of Google Patents")
    for link in list_google_patent:
        download_data(link)

    crawling_data_from_reedtech()

    logging.info("Starting Download of Reedtech Patents")
    for link in list_reedtech_patent:
        download_data(link)


