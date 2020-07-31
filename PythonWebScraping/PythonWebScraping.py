from bs4 import BeautifulSoup
import re
import urllib.request

pattern = re.compile('[0-9]+')

def parseContent():
    soup = BeautifulSoup(urllib.request.urlopen("http://hiphople.com/kboard").read(), "html.parser")
    for div in soup.find_all("tr", class_="notice"):
        div.decompose()

    key_num = pattern.findall(soup.find_all("td", class_="no")[0].text)
    category = soup.find_all("td", class_="categoryTD")[0].find("span").text
    author = soup.find_all("td", class_="author")[0].find("span").text
    title = soup.find_all("td", class_="title")[0].find("a").text
    link = "http://hiphople.com" + soup.find_all("td", class_="title")[0].find("a").attrs["href"]

    soup2 = BeautifulSoup(urllib.request.urlopen(link).read(), "html.parser")
    content = str(soup2.find_all("div", class_="article-content")[0].find_all("p"))
    content = re.sub("<.+?>","", content,0).strip()
    content = re.sub("\xa0","", content, 0).strip()

    result = {"key_num": key_num, "catetory": category, "title": title, "author": author, "content": content}
    yield result


while(True):
    print(parseContent())
