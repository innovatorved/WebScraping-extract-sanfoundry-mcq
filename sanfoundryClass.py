class copyit:

  def __init__(self , link):
    """Initialize Class by Sanfoundry link"""
    self.url = link
    from bs4 import BeautifulSoup
    import requests
    req = requests.get(self.url)
    soup = BeautifulSoup(req.text, "html.parser")
    self.title = soup.title.string
    print(self.title)

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
    self.mcq = mcq2

    i = 1
    self.mcqdict = {}
    for e in self.mcq:
      self.mcqdict[i] = e 
      i = i+1


  def copyright(self):
    """Copyright Information"""
    __author__ = "Ved Prakash Gupta"
    __copyright__ = f"Copyright (C) 2021 {__author__}"
    __license__ = "Public Domain"
    __version__ = "1.0"

  def extract_list(self):
    """MCQ Data in the form of list"""
    return self.mcq

  def extract_dict(self):
    """MCQ Data in dict form serial wise"""
    return self.mcqdict

  def extract_str(self):
    """MCQ String"""
    return "\n\n".join(self.mcq)

  def extract_pdf(self):
    """Save MCQ pdf"""
    mcq3 = "\n\n".join(self.mcq)
    f = open("data.txt" , "w")
    f.write(mcq3)
    f.close()
    from fpdf import FPDF
    pdf = FPDF(format='letter') #pdf format
    pdf.add_page() #create new page
    pdf.set_font("Courier", size=9) # font and textsize

    file1 = open("data.txt" , "r")
    data = file1.readlines()

    pdf.cell(200 , 10 , txt = str(f"{self.title}").encode('latin-1', 'replace').decode('latin-1') , ln = 1 , align="C")

    lineNum = 4
    for line in data:
      try : 
        pdf.cell(100 , 8 , txt = str(line).encode('latin-1', 'replace').decode('latin-1') , ln = lineNum , align="L")
        lineNum = lineNum + 1
      except:
        pass
    try :
      pdf.output(f"{self.title}.pdf")
    except Exception as e:
      print(e)
    return f"pdf Saved as {self.title}.pdf"
  
