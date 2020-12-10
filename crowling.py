import telegram

import requests
from bs4 import BeautifulSoup

req = requests.get("http://ncov.mohw.go.kr/")
#print(req.text)

soup = BeautifulSoup(req.text, "html.parser")
#print(soup)

국내, 해외 = soup.find("div",class_ = "liveNum_today_new").find_all("span", class_="data")

print("국내 발생 : \n", int(국내.text))
print("해외 발생 : \n", int(해외.text))
print("일일 확진자 : \n", int(국내.text)+int(해외.text))