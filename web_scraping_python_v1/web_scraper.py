# This python file has code for a web scraper for a static website
# This file follows demo : https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup    # BeautifulSoup is suitable fpr static websites web scraping

# Demo url we are going to web scrap
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# parsing html response using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# extracting the html by id
results = soup.find(id = "ResultsContainer")

# finding all div elements with class name = "card-content"
cards = results.find_all("div", class_ = "card-content")

print(len(cards)) # No. of all job listings = 100

# Extracting actual text from the html
for card in cards:
    title = card.find("h2", class_ = "title")
    subtitle = card.find("h3", class_ = "subtitle")
    location = card.find("p", class_ = "location")
    datetime = card.find("p", class_ = "is-small")
    print(title.text.strip())
    print(subtitle.text.strip())
    print(location.text.strip())
    print(datetime.text.strip())
    print("\n")


# Extracting jobs that have 'python' in their title
python_cards = results.find_all("h2",  string =lambda text: "python" in text.lower())

# finding parent  elements of the filtered python cards
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_cards
]

print(len(python_job_elements)) # No. of jobs that have 'python' in their job title = 10

for python_job in python_job_elements:
    title = python_job.find("h2", class_ = "title")
    subtitle = python_job.find("h3", class_ = "subtitle")
    location = python_job.find("p", class_ = "location")
    datetime = python_job.find("p", class_ = "is-small")
    learn_link =python_job.find("a", string = "Learn")['href'] #Extracting link from href attribute
    apply_link =python_job.find("a", string = "Apply")['href']

    print(title.text.strip())
    print(subtitle.text.strip())
    print(location.text.strip())
    print(datetime.text.strip())
    print(learn_link)
    print(apply_link)
    print("\n")