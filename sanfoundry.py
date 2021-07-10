#!/usr/bin/env python3

__author__ = "Ved Prakash Gupta"
__copyright__ = f"Copyright (C) 2021 {__author__}"
__license__ = "Public Domain"
__version__ = "1.0"

from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) == 2:
  url = sys.argv[1]
else:
  url = input("Enter the Sanfoundry Site Name : ")
# url = "https://www.sanfoundry.com/operating-system-questions-answers-basics/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title.string)

# sf-postw-category
divs = soup.find_all('div' , {"class": "sf-postw-category"})


os_link = []
dic = {}
for link in divs[0].find_all('a'):
  os_link.append(link.get('href'))
  dic[link.string] = link.get('href')

# Extract Data from Links
contain_pages = []
for link in os_link:
  req = requests.get(link)
  soup = BeautifulSoup(req.text, "html.parser")
  divs = soup.find_all('div' , {"class" : "entry-content"})
  contain_pages.append(divs[0])

contain_mcq_div = set({})
for x in contain_pages:
  div_mcq = x.find_all('p')
  for i in range(len(div_mcq)-1 , -1 , -1):
    e = str(div_mcq[i]).split("</div>")
    for ele in e:
      contain_mcq_div.add(ele)
    
mcq = []
for x in contain_mcq_div:
  try :
    vs = x.index("<span")
    s = x[:vs]
    i = x[x.index("<div"):]
    i = i[i.index(">"):]
    mcq.append(f"{s}\n{i}")
  except:
    pass

# Total tag
tags=["a","br","abbr","acronym","address","area","b","base","bdo","big","blockquote","body","br","button","caption","cite","code","col","colgroup","dd","del","dfn","div","dl","DOCTYPE","dt","em","fieldset","form","h1","h2","h3","h4","h5","h6","head","html","hr","i","img","input","ins","kbd","label","legend","li","link","map","meta","noscript","object","ol","optgroup","option","p","param","pre","q","samp","script","select","small","span","strong","style","sub","sup","table","tbody","td","textarea","tfoot","th","thead","title","tr","tt","ul","var"]
tag_list = []
for t in tags:
  t,t2,t3 = f"<{t}>" , f"</{t}>", f"<{t}/>"
  tag_list.append(t)
  tag_list.append(t2)
  tag_list.append(t3)
# print(tag_list)

mc = set(mcq)
mcq2 = []
for m in mc:
  for x in tag_list:
    try:
      m = m.replace(x , "")
    except:
      pass
  mcq2.append(m)


print(f"len is {len(mcq2)}")