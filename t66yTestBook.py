#pip install requests
#pip install beautifulsoup4
#pip install lxml
#pip install aiohttp
#pip install asyncio
#pip install cchardet
#pip install aiodns
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

async def decodeHtml(req):
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

#多线程打开页面


async def fetch(session, url):
    with async_timeout.timeout(60):
        async with session.get(url) as response:
            return await response.text()

async def downJob(subHtml):
    try:  # 加入try catch
       subSoup = BeautifulSoup(subHtml, 'lxml')
       words = subSoup.find_all("div", {"class": re.compile('tpc_content do_not_catch')})
#print(words)

 #获取title
       titleName = subSoup.title.string
       tIndex = titleName.index(" - 成人文學交流區")
       tName = titleName[0:tIndex]
    
       saveHtml="<html>%s</html>" % str(words)
       with open("c:/book/%s.html" % tName, "w") as f:
          f.write(saveHtml)

       print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
       print("saved %s " % tName)
    except Exception as e:
       print(e)  # 加入打印


async def asyncDown(session, str_link):
    try:  # 加入try catch
               if str_link == "htm_data/8/1106/524775.html":
                  return
               subURL = "http://t66y.com/" + str_link
               
               r = requests.get(subURL)
               html=await decodeHtml(r)
               await downJob(html)

               #html=await fetch(session,subURL)
               #await downJob(html)

    except Exception as e:
            print(e)  # 加入打印


async def run(loop,course_links):
    #conn = aiohttp.TCPConnector(family=socket.AF_INET,verify_ssl=False,)
    conn = aiohttp.TCPConnector(family=socket.AF_INET,verify_ssl=False,limit=1,use_dns_cache=False)
    async with aiohttp.ClientSession(loop=loop,connector=conn) as session:
          tasks = []
          for link in course_links:
              #task=loop.create_task(asyncDown(session,link['href']))
              tasks.append(asyncDown(session, link['href']))
          finished = await asyncio.wait(tasks)
          all_results = [r.result() for r in finished]    # 获取所有结果
          print(all_results)

def multiTime(urls):
        try:
           r=requests.get(urls)
           print(r.encoding)
           html = r.text
           soup = BeautifulSoup(html, 'lxml')
           course_links = soup.find_all("a", {"href": re.compile('.*?\.html')})
           if course_links == "[]":
               print("打开页面失败")
               
           t1 = time.time()
           loop = asyncio.get_event_loop()
           loop.run_until_complete(run(loop,course_links))
           #loop.close()                      # Ipython notebook gives error if close loop
           print("Async total time:", time.time() - t1)
        except Exception as e:
            print(e)  # 加入打印

if __name__ == "__main__":
    pool = mp.Pool(processes=10) #开启10个进程
    i = 1
    while i <= 100:
        URL = "http://t66y.com/thread0806.php?fid=20&search=&page=" + \
               str(i)
        print("Process Start")
        pool.map(multiTime,URL)
        p = mp.Process(target=multiTime, args=(URL,))
        i = i + 1
        p.start()
        p.join()
        print("Process end.")

print("Done")
