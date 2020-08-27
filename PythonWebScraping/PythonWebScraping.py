from bs4 import BeautifulSoup
import re
import urllib.request
from dataScrapping import parseContent
import time
 

pattern = re.compile('[0-9]+')

#원하는 페이지까지 크롤링 해주는 코드


#base_url = "http://hiphople.com/index.php?mid=kboard&page={}"

#for n in range(10):
#    soup = BeautifulSoup(urllib.request.urlopen(base_url.format(n+1)).read(), "html.parser")
#    for div in soup.find_all("tr", class_="notice"):
#        div.decompose()

#    key_num = soup.find_all("td", class_="no")
#    category = soup.find_all("span", class_="category")
#    author = soup.find_all("td", class_="author")
#    title = soup.find_all("td", class_="title")
#    link = soup.find_all("td", class_="title")

#    for x,y,z,t,u in zip(key_num, category, author, title, link):
#        hyperlink = "http://hiphople.com" + u.find("a").attrs["href"]
#        soup2 = BeautifulSoup(urllib.request.urlopen(hyperlink).read(), "html.parser")
#        content = str(soup2.find_all("div", class_="article-content")[0].find_all("p"))
#        content = re.sub("<.+?>","", content,0).strip()
#        content = re.sub("\xa0","", content, 0).strip()
#        print ({"number": x.text.strip(), "category": y.text.strip(), "author": z.text.strip(), "title": t.find("a").text.strip(), "content": content})


#스케줄링으로 일정 시간 동안 새로 올라온 글들만 크롤링 해주는 코드

#soup = BeautifulSoup(urllib.request.urlopen("http://hiphople.com/kboard").read(), "html.parser")
#for div in soup.find_all("tr", class_="notice"):
#    div.decompose()

#for n in range(0, 10):
#    key_num = pattern.findall(soup.find_all("td", class_="no")[n].text)
#    category = soup.find_all("td", class_="categoryTD")[n].find("span").text
#    author = soup.find_all("td", class_="author")[n].find("span").text
#    title = soup.find_all("td", class_="title")[n].find("a").text
#    link = "http://hiphople.com" + soup.find_all("td", class_="title")[n].find("a").attrs["href"]
#    soup2 = BeautifulSoup(urllib.request.urlopen(link).read(), "html.parser")
#    content = str(soup2.find_all("div", class_="article-content")[0].find_all("p"))
#    content = re.sub("<.+?>","", content,0).strip()
#    content = re.sub("\xa0","", content, 0).strip()

#    print(key_num, category, author, title, content)

def cronSched():

    temp = []
    soup_start = BeautifulSoup(urllib.request.urlopen("http://hiphople.com/kboard").read(), "html.parser")
    for div in soup_start.find_all("tr", class_="notice"):
        div.decompose()
    start = int(soup_start.find_all("td", class_="no")[0].text.strip())
    print(start)
    time.sleep(600)
    soup_end = BeautifulSoup(urllib.request.urlopen("http://hiphople.com/kboard").read(), "html.parser")
    for div in soup_end.find_all("tr", class_="notice"):
        div.decompose()
    end = int(soup_end.find_all("td", class_="no")[0].text.strip())
    print(end)

    len = end - start

    if len > 0:
        for n in range(0, len):

            key_num = pattern.findall(soup_end.find_all("td", class_="no")[n].text)
            category = soup_end.find_all("td", class_="categoryTD")[n].find("span").text
            author = soup_end.find_all("td", class_="author")[n].find("span").text
            title = soup_end.find_all("td", class_="title")[n].find("a").text
            link = "http://hiphople.com" + soup_end.find_all("td", class_="title")[n].find("a").attrs["href"]
            soup2 = BeautifulSoup(urllib.request.urlopen(link).read(), "html.parser")
            content = str(soup2.find_all("div", class_="article-content")[0].find_all("p"))
            content = re.sub("<.+?>","", content,0).strip()
            content = re.sub("\xa0","", content, 0).strip()

            temp.append(title)

            print(key_num, category, author, title, content)
    else:
        print("no newly created content")

while(True):
    cronSched()
