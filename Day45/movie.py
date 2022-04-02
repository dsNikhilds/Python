from bs4 import BeautifulSoup

import requests

url = "https://stacker.com/stories/1587/100-best-movies-all-time"

responses = requests.get(url)

web_text = responses.text
soup = BeautifulSoup(web_text,"html.parser")



#articles = soup.find_all(name="h3",class_="jsx-4245974604")
articles = soup.select(selector="div h2 div")
article_texts = []
# article_links = []

for item in articles:
    article_text = item.getText()
    article_texts.append(article_text[:-7])
article_texts

    
    
#article_score = [int(item.getText()[:-7])    for item in soup.find_all(name="span",class_="score")]

# print(article_links)
#print(article_texts)
# print(article_score)
   

# ind = article_score.index(max(article_score))

# print(article_texts[ind])
# print(article_links[ind])

movies = []
movies.extend(article_texts[1:])
movie_list = []
for i in movies:
    movie_list.append(i[1:])

movies = movie_list[::-1]

with open("movies.txt","w") as file:
    for movie in movies:
        file.write(f"{movie}\n")