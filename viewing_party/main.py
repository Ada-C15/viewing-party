# --------------------Wave 1--------------------------

def create_movie(movie_title, genre, rating):
    # create dictionary
    new_movies = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }
    # if title, genre, rating are true:
    if movie_title and genre and rating:
        return new_movies
    # return dictionary
    else:
        return None
    # else:
        # return None

def add_to_watched(user_data, movie):
    # add the new movie to the users data's watched dictionary
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # loop through user_data:
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
        # remove movie_title from watchlist
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    # return user_data
    return user_data

# # -----------------------Wave 2-------------------------

def get_watched_avg_rating(user_data):

    watched_list = user_data["watched"]
    rating_list = []

    for movie in watched_list:
        rating_list.append(movie["rating"])
    if len(rating_list) == 0:
        avg_rating = 0.0
        return avg_rating
    else:
        avg_rating = sum(rating_list)/ len(rating_list)
        return avg_rating

def get_most_watched_genre(user_data):

    most_watched = {}
    popular_genre = None

    for movie in user_data["watched"]:
        if movie["genre"] not in most_watched:
            most_watched[movie["genre"]] = 1
        else:
            most_watched[movie["genre"]] += 1
        popular_genre = max(most_watched, key = most_watched.get)
    return popular_genre


#     # -------------------Wave 3---------------------------


def get_unique_watched(user_data):

    users_unique_movies = []
    friends_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)

    for movie in user_data["watched"]:
        if movie not in friends_movies:
            users_unique_movies.append(movie)
    
    return users_unique_movies

def get_friends_unique_watched(user_data):

    friends_unique_movies = []
    users_movies = []

    for movie in user_data["watched"]:
        users_movies.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in users_movies:
                if movie not in friends_unique_movies:
                    friends_unique_movies.append(movie)
    
    return friends_unique_movies


# ---------------------Wave 4---------------------------

def get_available_recs(user_data):    

    friends_movies = user_data["friends"]
    subscriptions = user_data["subscriptions"]
    recommendations = []

    for friend in friends_movies:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and\
            movie not in recommendations and\
            movie["host"] in subscriptions:
                recommendations.append(movie)

    for movie in recommendations:
        # if host, service not in recommendations:
        if movie["host"] not in subscriptions:
            recommendations.remove(movie)
    # if len(user_data["watched"]) == 0:
    #     return []

    return recommendations

# ---------------------Wave 5---------------------------

def get_new_rec_by_genre(user_data):

    # assign results of get_most_watched_genre to a variable
    user_genre = get_most_watched_genre(user_data)
    friends_movies = user_data["friends"]
    recommendations = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == user_genre:
                recommendations.append(movie)
    
    return recommendations

def get_rec_from_favorites(user_data):

    user_favories = user_data["favorites"]
    friends_movies = user_data["friends"]
    favorites = []
    user_rec = []

    for movie in user_favories:
        favorites.append(movie)

    for movie in favorites:
        for movie in friends_movies["watched"]:
            # if movie not in friends_movies["watched"]:
            user_rec.append(movie)

    return user_rec

def get_rec_from_favorites(user_data):

    user_favories = user_data["favorites"]
    friends_movies = user_data["friends"]
    favorites = []
    friend_watched = []
    user_rec = []

    for movie in user_favories:
        favorites.append(movie)

    for friend in friends_movies:
        for movie in friend["watched"]:
            friend_watched.append(movie)

    for movies in favorites:
        if movies not in friend_watched:
            user_rec.append(movies)
    
    return user_rec