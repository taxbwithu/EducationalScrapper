import requests
from bs4 import BeautifulSoup
import re

from Movie import *


class Extractor:

    def get_site(self):
        url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        movies = []
        movie_titles = []
        duration = []
        rating = []
        year = []
        director = []
        number_of_votes = []

        for item in soup.findAll('h3', attrs={'class': 'lister-item-header'}):
            movie_titles.append(item.find('a').contents[0])
        for item in soup.findAll('span', attrs={'class': 'runtime'}):
            duration.append(item.contents[0])
        for item in soup.findAll('div', attrs={'class': 'inline-block ratings-imdb-rating'}):
            rate = float(item.find('strong').contents[0])
            rating.append(rate)
        for item in soup.findAll('span', attrs={'class': 'lister-item-year text-muted unbold'}):
            current_year = item.contents[0].replace('(', '').replace(')', '').replace('I ', '')
            year.append(int(current_year))
        for item in soup.findAll('p', attrs={'class': ''}):
            director.append(item.find('a').contents[0])
        for item in soup.findAll('p', attrs={'class': 'sort-num_votes-visible'}):
            vote = item.find('span', {"name": "nv"}).contents[0].replace(',', '')
            vote_number = int(vote)
            number_of_votes.append(vote_number)

        for (title, duration, rating, year, director, no_votes) in zip(movie_titles,duration,rating,year,director,number_of_votes):
            movies.append(Movie(title,duration,rating,year,director,no_votes))

        return movies
