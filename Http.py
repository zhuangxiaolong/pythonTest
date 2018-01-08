
from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen
import re
import time
import aiohttp
import asyncio
import async_timeout
import socket # together with your other imports
import multiprocessing as mp

os.makedirs('c:/book/', exist_ok=True)

def decodeHtml(req):
 if req.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(req.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = req.apparent_encoding

    # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    global encode_content
    encode_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；
    return encode_content

subURL="http://t66y.com/htm_data/20/1801/2899297.html"
r=requests.get(subURL)
html= decodeHtml(r)
subSoup = BeautifulSoup(html, 'lxml')
words = subSoup.find_all("div", {"class": re.compile('tpc_content do_not_catch')})
#print(words)

 #获取title
titleName=subSoup.title.string
tIndex=titleName.index(" - 成人文學交流區")
tName=titleName[0:tIndex]

#os.mknod("c:/book/%s.txt" %tName)        #创建空文件
saveHtml="<html>%s</html>" % str(words)
print(saveHtml)
with open("c:/book/%s.txt" %tName, "w") as f:
          f.write(str(words))