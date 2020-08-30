from bs4 import BeautifulSoup
import re
import urllib.request
from dataScrapping import parseContent
import time
import json
 

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


######## HIPHOPLE에 새로운 글이 올라오면 스크랩해서 return 하는 함수 ###########

def ScrapLE():
    difference = 0
    output = []

    soup_start = BeautifulSoup(urllib.request.urlopen("http://hiphople.com/kboard").read(), "html.parser")
    for div in soup_start.find_all("tr", class_="notice"):
        div.decompose()
    title_temp = soup_start.find_all("td", class_="title")

    time.sleep(600)

    soup_end = BeautifulSoup(urllib.request.urlopen("http://hiphople.com/kboard").read(), "html.parser")
    for div in soup_end.find_all("tr", class_="notice"):
        div.decompose()
 
    title_compare = soup.end.find_all("td", class_="title")

    for n in range(0, len(title_compare)):
        if title_compare[n] not in title_temp:
            key_num = pattern.findall(soup_end.find_all("td", class_="no")[n].text)
            category = soup_end.find_all("td", class_="categoryTD")[n].find("span").text
            author = soup_end.find_all("td", class_="author")[n].find("span").text
            title = soup_end.find_all("td", class_="title")[n].find("a").text
            link = "http://hiphople.com" + soup_end.find_all("td", class_="title")[n].find("a").attrs["href"]
            soup2 = BeautifulSoup(urllib.request.urlopen(link).read(), "html.parser")
            content = str(soup2.find_all("div", class_="article-content")[0].find_all("p"))
            content = re.sub("<.+?>","", content,0).strip()
            content = re.sub("\xa0","", content, 0).strip()
            output.append({"number": key_num, "category": category, "author": author, "title": title, "content": content})
            difference += 1
    
    if difference > 0:
        for str in output:
            yield str
    else:
        return "there is no newly created content"

######## 루리웹에 새로운 글이 올라오면 스크랩해서 return 하는 함수 ###########
def scrapRuliweb():
    temp = []
    output = []
    result = []
    soup1 = BeautifulSoup(urllib.request.urlopen("https://bbs.ruliweb.com/best/board/300143").read(), "html.parser")
    soup_start = soup1.find("div", class_= "board_main theme_default")

    for div in soup_start.find_all("tr", class_="table_body notice inside"):
        div.decompose()
    for div in soup_start.find_all("tr", class_="table_body best inside"):
        div.decompose()
    for div in soup_start.find_all("tr", class_="table_body list_inner"):
        div.decompose()

    title_temp = soup_start.find_all("div", class_="relative")

    for title in title_temp:
        temp.append(title.find("a").text.strip())

    time.sleep(60)
    
    soup2 = BeautifulSoup(urllib.request.urlopen("https://bbs.ruliweb.com/best/board/300143").read(), "html.parser")
    soup_last = soup2.find("div", class_= "board_main theme_default")

    for div in soup_last.find_all("tr", class_="table_body notice inside"):
        div.decompose()
    for div in soup_last.find_all("tr", class_="table_body best inside"):
        div.decompose()
    for div in soup_last.find_all("tr", class_="table_body list_inner"):
        div.decompose()

    key_num = soup_last.find_all("td", class_="id")
    category = soup_last.find_all("td", class_="divsn")
    author = soup_last.find_all("td", class_="writer text_over")
    title = soup_last.find_all("div", class_="relative")
    link = soup_last.find_all("div", class_="relative")
       
    for x, y, z, t, u in zip (key_num, category, author, title, link):
        hyperlink = u.find("a").attrs["href"]
        soup2 = BeautifulSoup(urllib.request.urlopen(hyperlink).read(), "html.parser")
        content = str(soup2.find_all("div", class_="view_content")[0].find("div"))
        content = re.sub("<.+?>","", content,0).strip()
        content = re.sub("\xa0","", content, 0).strip()
        output.append({"number": x.text.strip(), "category": y.text.strip(), "author": z.find("a").text.strip().replace('\xad', ''), "title": t.find("a").text.strip(), "content": content.replace('\n', '')})
    
    

    for check in output:
        if check["title"] not in temp:
            result.append(check)

    if len(result) > 0:
        for string in result:
            yield string
    else:
        return "there is no newly created content"
    
############ 루리웹 첫 페이지 스크랩 테스트용 함수 ########
def checkRuliweb():
    soup = BeautifulSoup(urllib.request.urlopen("https://bbs.ruliweb.com/best/board/300143").read(), "html.parser")
    soup_end = soup.find("div", class_= "board_main theme_default")

    for div in soup_end.find_all("tr", class_="table_body notice inside"):
        div.decompose()
    for div in soup_end.find_all("tr", class_="table_body best inside"):
        div.decompose()
    for div in soup_end.find_all("tr", class_="table_body list_inner"):
        div.decompose()

    key_num = soup_end.find_all("td", class_="id")
    category = soup_end.find_all("td", class_="divsn")
    author = soup_end.find_all("td", class_="writer text_over")
    title = soup_end.find_all("div", class_="relative")
    link = soup_end.find_all("div", class_="relative")
       
    for x, y, z, t, u in zip (key_num, category, author, title, link):
        hyperlink = u.find("a").attrs["href"]
        soup2 = BeautifulSoup(urllib.request.urlopen(hyperlink).read(), "html.parser")
        content = str(soup2.find_all("div", class_="view_content")[0].find("div"))
        content = re.sub("<.+?>","", content,0).strip()
        content = re.sub("\xa0","", content, 0).strip()
        yield {"number": x.text.strip(), "category": y.text.strip(), "author": z.find("a").text.strip().replace('\xad', ''), "title": t.find("a").text.strip(), "content": content.replace('\n', '')}




#while(True):
#    temp = scrapRuliweb()
#    for i in temp:
#        print(i)
#    print("#################################################################################################################################################################")
