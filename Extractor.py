import requests
from bs4 import BeautifulSoup
import re

class Extractor:

    def getSite():
        url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        movie_titles = []
        duration = []
        rating = []
        year = []
        director = []
        number_of_votes = []

        for div in soup.findAll('h3', attrs={'class': 'lister-item-header'}):
            movie_titles.add(div.find('a').contents[0])