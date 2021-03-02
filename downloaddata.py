from urllib import request
import urllib.request

url_dwn= "http://patents.reedtech.com/downloads/ApplicationFullText/2016/ipa160407.zip"
def download_data(patent_url):
    # response= request.urlopen(patent_file)
    # patent = response.read()
    # f_str= str(patent)
    # lines= f_str.split("\\n")
    #
    # fx= open(dest_url,"w")
    # for line in lines:
    #     fx.write(line + "\n")
    # fx.close()

    print("Start Download")
    file_name = url_dwn.split("/")[-1]
    fname, header = urllib.request.urlretrieve(patent_url, file_name)
    print ("End Download")


download_data(url_dwn)