from bs4 import BeautifulSoup

#read our html file
with open('website.html') as file:
    contents = file.read()

#pass in html contents and parse it to be readable
soup = BeautifulSoup(contents, "html.parser")
# we can scrape parts of the website by printing tags from html

#get title
print(soup.title.string)
#get anchor tag
print(soup.a)
#get p tag
print(soup.p)

#get all p tags (can do find_all with any tags)
all_p_tags = soup.find_all(name="p")
print(all_p_tags)

#gets text in all p tags
for tag in all_p_tags:
    print(tag.getText())

#gets tag by tag name and id 
heading = soup.find(name='h1', id='name')
print(heading)

#gets tag by tag name and class
sub_heading = soup.find(name='h3', id='heading')
print(sub_heading)

#get anchor tag inside p tag
company_url = soup.select_one(selector='p a')
print(company_url)

#SCRAPING A LIVE WEBSITE

import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
 
news = soup.find_all(class_="titleline")
for heading in news:
    print(heading.find(name="a").get("href"))
    print(heading.find(name="a").getText())
 
scores = soup.find_all(class_="score")
for score in scores:
    print(score.getText().split(" ")[0])


