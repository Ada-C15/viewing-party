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
        return mean(movie['rating'] for movie in user_data['watched']) 
        # list comprehension replaces for loop
    else:
        return 0

def get_most_watched_genre(user_data):
    if not user_data['watched']:
        return None
    else:
        genre_list = [item['genre'] for item in user_data['watched']]
        # returns each genre in a list
        genre_count = Counter(genre_list).most_common() 
        # creates an unordered collection of data with count information from python's
        #  built in Counter from collections module
        return genre_count[0][0]

def get_unique_watched(user_data):
    # gets movies that user has watched that user's friends haven't
    user_watched = [x for x in user_data['watched']]
    unique_watched = []
    friend_watched = []
    for friend_data in user_data["friends"]:
        for watched_key, movies in friend_data.items():
            for movie in movies:
                friend_watched.append(movie)
    for movie in user_watched:
        if movie not in friend_watched and movie not in unique_watched:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    # gets movies that friends have watched but user hasn't
    user_watched = [x for x in user_data['watched']]
    unique_watched = []
    friend_watched = []
    for friend_data in user_data["friends"]:
        for watched_key, movies in friend_data.items():
            for movie in movies:
                friend_watched.append(movie)
    for movie in friend_watched:
        if movie not in user_watched and movie not in unique_watched:
            unique_watched.append(movie)
    return unique_watched
