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
        for description, value in dict.items():
            if description == "genre":
                if value in genre_tally:
                    genre_tally[value] += 1
                else:
                    genre_tally[value] = 1
            elif description == None:
                return None

    for genre, tally_count in genre_tally.items():
        if True:
            all_values = genre_tally.values()
            max_value = max(all_values)
            if tally_count == max_value:
                return genre

def get_watched_avg_rating(user_data):
    rating_total = 0
    ratings = []
    movie_list = user_data["watched"]

    if movie_list != []:
        for dict in movie_list:
            for description, value in dict.items():
                if description == "rating":
                    rating_total += dict[description]
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
    friends_values = user_data["friends"]

    for movie in user_watched_values:
        user_watched_list.append(movie)

    for friend in friends_values:
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
    friends_values = user_data["friends"]

    for movie in user_watched_values:
        user_watched_list.append(movie)

    for friend in friends_values:
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
            for product in movie.values():
                if product in user_data["subscriptions"]:
                    available_recs_list.append(movie)

    return available_recs_list

"""
get_friends_watched is a funciton that compiles a list
of all the movies that the user's friends have watched
as noted in their 'watched' lists.
"""
def get_friends_watched(user_data):
    friends_watched_list = []
    user_friends_values = user_data["friends"]

    for friend in user_friends_values:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    return friends_watched_list

def get_new_rec_by_genre(user_data):
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_watched(user_data)
    recommendation_list = []

    if user_data["watched"] != []:
        for movie in friends_watched_list:
            if movie not in user_watched_list:
                recommendation_list.append(movie)
        return recommendation_list
    else:
        return recommendation_list

def get_rec_from_favorites(user_data):
    friends_watched = get_friends_watched(user_data)
    available_recs_list = []
    user_favorite_list = user_data["favorites"]

    if user_data["watched"] != []:
            for movie in user_favorite_list:
                if movie in friends_watched:
                    continue
                else:
                    available_recs_list.append(movie)
                return available_recs_list
    else:
        return available_recs_list