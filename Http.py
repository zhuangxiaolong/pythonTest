from urllib.request import urlopen
import re

#if has chinese, apply decode()
html=urlopen("https://douban.fm/").read().decode("utf-8")
print(html)

res=re.findall(r"<title>(.+?)</title>",html)
print("\nPage title is:",res[0])

res2=re.findall(r"<p>(.*?)</p>",html,flags=re.DOTALL)
print("\n Page reagraph is:",res2[0])