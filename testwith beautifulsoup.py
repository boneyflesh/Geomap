import requests
import re
from bs4 import BeautifulSoup

urls = ["http://www.phivolcs.dost.gov.ph/index.php?option=com_content&view=article&id=7029:mayon-volcano-bulletin-30-january-2017-800-am-&catid=70:latest-volcano-bulletin&Itemid=500008"]
unum=0
while unum<len(urls):    
    response = requests.get(urls[unum])
    txt = response.content
    soup = BeautifulSoup(txt,"lxml")

    Store=[]
     
    
    #print(soup)

    geohazardterms = ["lava","lava flow","ablation till","accretion","Volcano"]

    table = soup.findAll('tr')
    i=0
    x=0

    while(i != len(table)):   
        if any(words in table[i].get_text() for words in geohazardterms):
            print(table[i].get_text())
            striped=table[i].get_text()
            Store.append(re.sub('<[^>]*>', '', striped).replace('\n',''))
        i+=1
  
    paragraph = soup.findAll('p')
    
    while(x != len(paragraph)):
        
        if any(words in paragraph[x].get_text() for words in geohazardterms):
            checkS = paragraph[x].get_text()
            checkS = re.sub('<[^>]*>', '', checkS).replace('\n','')
            if any(checkS in phrase for phrase in Store ):             
                print("Sorry pariha ra")
            else:                
                print(paragraph[x].get_text())
                Store.append(checkS)      
        x+=1

    print Store
    print len(Store)
    
    unum+=1
    


