import os
import requests
from bs4 import BeautifulSoup


MY_URL = "http://web.archive.org/web/20240718014239/https://www.listchallenges.com/100-best-korean-drama"


response = requests.get(url=MY_URL)
dramas_webpage = response.text


soup = BeautifulSoup(dramas_webpage, "html.parser")
title_list = soup.find_all(class_="item-name")
# print(title_list.getText().strip())


titles = [title.getText().strip() for title in title_list]
print(titles)

with open("movies.txt", mode="w", encoding="utf-8") as dramas_file:
    for title in titles:
        dramas_file.write(f"{title}\n")





