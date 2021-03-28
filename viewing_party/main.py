import pytest
from pytest import approx

# create_movie function
def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    return {"title": movie_title, "genre": genre, "rating": rating}

# add_to_watched function
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# add_to_watchlist function
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# watch_movie function
def watch_movie(user_data, movie):
    watchlist = user_data["watchlist"]
    watchedlist = user_data["watched"]
    for data in watchlist:
        if data["title"] == movie:
            watchlist.remove(data)
            watchedlist.append(data)
    return user_data

# get_most_watched_genre function
def get_most_watched_genre(user_data):
    genre_tally = {}
    movie_list = user_data["watched"]

    for dict in movie_list:
        for key, value in dict.items():
            if key == "genre":
                if value in genre_tally:
                    genre_tally[value] += 1
                else:
                    genre_tally[value] = 1
            elif key == None:
                return None

    for key, value in genre_tally.items():
        if True:
            all_values = genre_tally.values()
            max_value = max(all_values)
            if value == max_value:
                return key

# get_watched_avg_rating function
def get_watched_avg_rating(user_data):
    rating_total = 0
    ratings = []
    movie_list = user_data["watched"]

    if movie_list != []:
        for dict in movie_list:
            for key, value in dict.items():
                if key == "rating":
                    rating_total += dict[key]
                    ratings.append(value)
        avg_rating = pytest.approx(rating_total/len(ratings))
        return avg_rating
    else:
        return 0

amandas_data = {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            },
            {
                "title": "Title D"
            },
            {
                "title": "Title E"
            },
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title D"
                    },
                    {
                        "title": "Title F"
                    }
                ]
            }
        ]
    }
def get_unique_watched(user_data):
    friends_watched = set()
    users_watch = set()
    
    # returns movies that aren't in other people's data (parses over user_data first)
    # user_data is a dictionary with 2 key-value pairs. (key 1: watched (for jane) 
    # & key 2: friends)
    # value for watched is a list filled with 2 dictionaries of watched movies
    # from other friends
    
get_unique_watched(amandas_data)

