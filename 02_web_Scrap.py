import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

headers=headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko)'
' Chrome/80.0.3987.162 Safari/537.36'}

final=pd.DataFrame()

for j in range(1,504):
    url= 'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={}'.format(j)

    webpage = requests.get(url,headers=headers).text

    soup = BeautifulSoup(webpage,features='html.parser')

    company =soup.find_all('div',class_='companyCardWrapper')

    name=[]
    rating=[]
    rating_count_k=[]
    domain=[]
    hq=[]
    locations=[]

    for i in company:

        #company name
        # print(i.find('h2',class_='companyCardWrapper__companyName').text.strip())
        name.append(i.find('h2',class_='companyCardWrapper__companyName').text.strip())

        #rating
        #print(i.find('div',class_='rating_text').text.strip())
        try:
            rating.append(i.find('div',class_='rating_text').text.strip())
        except:
            rating.append('nan')

        # total rating in thousands
        #print(i.find('span',class_='companyCardWrapper__companyRatingCount').text.strip()[1:-1])
        try:
            rating_count_k.append(i.find('span',class_='companyCardWrapper__companyRatingCount').text.strip()[1:-1])
        except:
            rating_count_k.append('nan')

        #domain
        #print(i.find('span',class_="companyCardWrapper__interLinking").text.strip().split("|")[0])
        domain.append(i.find('span',class_="companyCardWrapper__interLinking").text.strip().split("|")[0])

        #head quater
        #print(i.find('span',class_="companyCardWrapper__interLinking").text.strip().split("|")[1].split(" ")[1])
        try:
            hq.append(i.find('span',class_="companyCardWrapper__interLinking").text.strip().split("|")[1].split("+")[0])
        except:
            hq.append('nan')

        # locations
        #print(i.find('span',class_="companyCardWrapper__interLinking").text.strip().split("+")[1].split(" ")[0])
        try:
            locations.append(i.find('span',class_="companyCardWrapper__interLinking").text.strip().split("+")[1].split(" ")[0])
        except:
            locations.append('nan')

    d={'company_name':name,
    "rating":rating,
    "total rating in k":rating_count_k,
    "domain":domain,
    "head quater":hq,
    "locations":locations}

    df = pd.DataFrame(d)

    df.to_csv('output.csv',mode='a',                    # append mode
        index=False,
        header=(i == 0) )

    # final = pd.concat([final,df],ignore_index=True)
    print("done upto ",j)


# print(final.shape)
# final.to_csv('ambition_data.csv')