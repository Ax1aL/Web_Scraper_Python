from bs4 import BeautifulSoup
import requests

f=open("test.txt","w")

URL="http://www.thetherapist.com/Appointments.html"
page=requests.get(URL)

soup=BeautifulSoup(page.content,'html.parser')
result=soup.find('h3').find_all('a')
for i in result:
    URL="http://www.thetherapist.com/"+i['href']
    print(URL)
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    url2Result=soup.find_all('tt')
    for z in url2Result:
        url2Result2=z.find_all('a')
        for x in url2Result2:
            URL = URL[:URL.rfind("/")] + '/' + x['href']
            if URL.rfind('..') != -1:
                URL = URL[:URL.rfind("..")]+x['href'][x['href'].rfind('/')+1:]

            page=requests.get(URL)
            soup=BeautifulSoup(page.content,'html.parser')
            res=soup.find_all('td',width="328")
            for h in res:
                if h.string==None:
                    continue
                if h.string.strip()=="###":#we can add somethign to mark the end of the file
                    f.write("\n\n")
                    continue
                f.write(h.string.strip().replace('\n',' '))
                f.write("\n")
f.close()