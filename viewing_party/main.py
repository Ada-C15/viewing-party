from statistics import mean # new requirement 
from collections import Counter # built in to python

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        return {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
    return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for item in user_data['watchlist']:
        if movie == item['title']:
            user_data['watched'].append(item)
            user_data['watchlist'].remove(item)
    return user_data

def get_watched_avg_rating(user_data):
    if user_data['watched']:
        # using mean() from statistics since numpy mean() takes Array, not List
        return mean(movie['rating'] for movie in user_data['watched']) # list comprehension replaces for loop
    else:
        return 0

def get_most_watched_genre(user_data):
    if not user_data['watched']:
        return None
    else:
        genre_list = [item['genre'] for item in user_data['watched']]
        # returns each genre in a list
        genre_count = Counter(genre_list).most_common() 
        # creates an unordered collection of data with count information from python's built in Counter from collections module
        return genre_count[0][0]
        