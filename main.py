import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

result = []
titles = soup.find_all(name="h3", class_="title")
for title in titles:
    txt = title.getText()
    try:
        lst_txt = txt.split(") ")
        txt = lst_txt[1]
    except:
        lst_txt = txt.split(": ")
        txt = lst_txt[1]
    result.append(txt)
result.reverse()
with open("movies.txt", "w", encoding="utf-8") as file:
    i = 1
    for title in result:
        file.write(f"{i}) {title}\n")
        i += 1


