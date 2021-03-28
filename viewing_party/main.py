import pytest
from pytest import approx 

def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    return {"title": movie_title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    watchlist = user_data["watchlist"]
    watchedlist = user_data["watched"]

    for data in watchlist:
        if data["title"] == movie:
            watchlist.remove(data)
            watchedlist.append(data)
    return user_data

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

def get_unique_watched(user_data):
    unique_watched_list = []
    user_watched_list = []
    friends_watched_list = []
    user_watched_values = user_data["watched"]
    user_friends_values = user_data["friends"]

    for movie in user_watched_values:
        user_watched_list.append(movie)

    for friend in user_friends_values:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    for movie in user_watched_list:
        if movie not in friends_watched_list:
            unique_watched_list.append(movie)

    return unique_watched_list

def get_friends_unique_watched(user_data):
    unique_watched_list = []
    user_watched_list = []
    friends_watched_list = []
    user_watched_values = user_data["watched"]
    user_friends_values = user_data["friends"]

    for movie in user_watched_values:
        user_watched_list.append(movie)

    for friend in user_friends_values:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    for movie in friends_watched_list:
        if movie not in user_watched_list:
            if movie in unique_watched_list:
                continue
            else:
                unique_watched_list.append(movie)

    return unique_watched_list

def get_available_recs(user_data):
    friend_watched_list = (get_friends_unique_watched(user_data))
    available_recs_list = []

    for movie in friend_watched_list:
        if movie not in user_data["watched"]:
            for description, product in movie.items():
                if product in user_data["subscriptions"]:
                    available_recs_list.append(movie)

    return available_recs_list


# amandas_data = {
#         "subscriptions": ["Service A", "Service B"],
#         "watched": [],
#         "friends": [
#             {
#                 "watched": [
#                     {
#                         "title": "Title A",
#                         "host": "Service A"
#                     },
#                     {
#                         "title": "Title C",
#                         "host": "Service C"
#                     }
#                 ]
#             },
#             {
#                 "watched": [
#                     {
#                         "title": "Title A",
#                         "host": "Service A"
#                     },
#                     {
#                         "title": "Title B",
#                         "host": "Service B"
#                     },
#                     {
#                         "title": "Title D",
#                         "host": "Service D"
#                     }
#                 ]
#             }
#         ]
#     }


# get_available_recs(amandas_data)