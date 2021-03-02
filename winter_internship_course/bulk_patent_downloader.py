import urllib.request
import logging


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
    url_dwn = "http://patents.reedtech.com/downloads/ApplicationFullText/2016/ipa160407.zip"
    download_data(url_dwn)
