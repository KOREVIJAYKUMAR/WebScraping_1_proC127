from selenium import webdriver 
from bs4 import BeautifulSoup
import time
import csv

browser= webdriver.Chrome('chromedriver.exe')
url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser.get(url)

time.sleep(3)

def scrape():
    headers=['proper_name','distance','mass','radius']
    data=[]
    
    soup=BeautifulSoup(browser.page_source,"html.parser")
    trTags=soup.find_all("tr")
    trTags=trTags[1:]
   
     
     
    
    for tr in trTags:
        temp=[]
        tdTags=tr.find_all("td")
        
       

        for index,td in enumerate(tdTags) :
            try:
                if index==1:
                    temp.append(td.find_all('a')[0].contents[0])

                elif index==3:
                    temp.append(td.contents[1].rstrip())
                elif index==5:
                    temp.append(td.contents[0].rstrip())
                elif index==6:
                    temp.append(td.contents[0].rstrip())
                
            except:
                temp.append("")

        data.append(temp)   

        

    with open('scraped1.csv','w',newline="") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        try:

            csvwriter.writerows(data)
        except:
            pass
        
scrape()