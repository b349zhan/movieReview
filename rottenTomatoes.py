import re
import requests
from bs4 import BeautifulSoup
# import mechanicalsoup
# url = "https://www.rottentomatoes.com/m/joker_2019/reviews?type=&sort={}"
# browser = mechanicalsoup.Browser()
# totalPageNumber = 29
# reviews = []
# for i in list(range(totalPageNumber)):
#     page = browser.get(url.format(i+1))
#     soup = page.soup
#     resultSet = soup.find_all("div",class_="the_review")
#     for i in resultSet:
#         contents = i.contents
#         reviews.append(contents[0])
# print(reviews)

#
# url = 'http://quotes.toscrape.com/page/1/'
# page = requests.get(url)
# soup = BeautifulSoup(page.content,features='html.parser')
# t = soup.find_all('div',class_='quote')
# p = {}
# for quote in t:
#     words = quote.find('span',class_='text').text
#     author = quote.find('small',class_='author').text
#     tags = [x.text for x in quote.find_all('a',class_='tag')]
#
#     p[author]=[words,tags]
# h = 1
import pytube
import cv2

print(pytube.__version__)
video = pytube.YouTube('https://www.youtube.com/watch?v=HXV3zeQKqGY')
h = video.streams.filter(file_extension="mp4").all()
video.streams.get_by_itag(22).download(output_path="./")
t = 1
