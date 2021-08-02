import requests
import re
from bs4 import BeautifulSoup

if __name__ == "__main__":
    RANK = 50

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=481325782', headers=header)  ## 주간 차트를 크롤링 할 것임
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')

    title = []
    id = []

    for tag in parse.select('#pageList a[href*=goSongDetail]'):
        js = tag['href']
        matched = re.search("(\d+)",js)
        if matched:
            song_Id = matched.group(1)
            id.append(song_Id)

    titles = parse.find_all("div", {"class": "ellipsis rank01"})

    for t in titles:
        tt = t.find('a').text.replace(",", "")
        title.append(tt)

    f = open("test.csv", "w")
    f.write("id,title,mood \n")

    for i in range(RANK):
        f.write(id[i] + "," + title[i] + "," + 'excited' + "\n")

    f.close()