from urllib import request
import zipfile
# import os
fname1 = "http://www.finchpark.com/bookszip/tell-me-more-Korea/korea-tmm-student.zip"
# if os.path.isfile(fname1):
response = request.urlopen(fname1)
with zipfile.ZipFile(fname1, "r") as f:
    f.extractall("Desktop\\tester2016")
