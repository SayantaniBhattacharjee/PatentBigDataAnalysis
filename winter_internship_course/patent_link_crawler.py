
from urllib.request import urlopen
from bs4 import BeautifulSoup

list1 = []
list2=[]

def crawling_data_from_reedtech():
    reedtech_grant_fulltext_url = "http://patents.reedtech.com/pgrbft.php"
    reedtech_application_fulltext_url = "http://patents.reedtech.com/parbft.php"
    grant_page = urlopen(reedtech_grant_fulltext_url)
    application_page = urlopen(reedtech_application_fulltext_url)
    soup_grant = BeautifulSoup(grant_page.read(), 'html.parser')
    soup_application = BeautifulSoup(application_page.read(), 'html.parser')

    for patent_link in soup_grant.findAll('a'):
        if patent_link['href'].endswith('.zip'):
            list1.append("http://patents.reedtech.com/" + patent_link['href'])
    print(list1)
            # print ("http://patents.reedtech.com/" + patent_link['href'])
    for patent_link in soup_application.findAll('a'):
        if patent_link['href'].endswith('.zip'):
            list2.append("http://patents.reedtech.com/" + patent_link['href'])
    print (list2)
            #print ("http://patents.reedtech.com/" + patent_link['href'])


crawling_data_from_reedtech()
