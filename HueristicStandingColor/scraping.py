import requests
import time
from bs4 import BeautifulSoup
AlgoRating = []

searchUpperBound = 9999
searchLowerBound = 1200
for i in range(1,1000):
    url = f'https://atcoder.jp/ranking/all?f.Country=JP&contestType=algo&f.RatingUpperBound={searchUpperBound}&page={i}'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    isLower = 0
    for e in soup.select("tr"):
        if len(e.select("td")) < 4:
            continue
        if len(e.select("td")[1].select("span")) == 0:
                continue
        if len(e.select("td")[3].select("b")) == 0:
            continue
        username = e.select("td")[1].select("span")[0].text
        rating = e.select("td")[3].select("b")[0].text
        if int(rating) < int(searchLowerBound):
            isLower = 1
        # {"ogawakun" : "1604"}
        print(f'"{username}" : "{rating}",')
    if isLower == 1:
        break
    time.sleep(1)
