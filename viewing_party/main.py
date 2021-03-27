from statistics import mean


def create_movie(movie_title, genre, rating):
    if movie_title is None or genre is None or rating is None:
        return None 

    return {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data


def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0

    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])

    return mean(ratings)


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    genres = {}
    for movie in user_data["watched"]:
        for k, v in movie.items():
            if k == "genre":
                if v in genres:
                    genres[v] += 1
                else:
                    genres[v] = 1 

    count = 0
    most_watched = ""

    for k, v in genres.items():
        if v > count:
            count = v
            most_watched = k 

    return most_watched


def get_unique_watched(user_data):
    watched_source = user_data["watched"] 
    friend_1 = user_data["friends"][0]["watched"]
    friend_2 = user_data["friends"][1]["watched"]
    
    unique_movies = []
    for movie in watched_source:
        if movie not in friend_1 and movie not in friend_2:
            unique_movies.append({"title": movie["title"]})
            
    return unique_movies


def get_friends_unique_watched(user_data):
    watched_source = user_data["watched"] 
    friend_1 = user_data["friends"][0]["watched"]
    friend_2 = user_data["friends"][1]["watched"]

    friends_unique_movies = []
    for movie in friend_1:
        if movie not in watched_source:
            friends_unique_movies.append({"title": movie["title"]})
    
    for movie in friend_2:
        if movie not in watched_source and movie not in friends_unique_movies:
            friends_unique_movies.append({"title": movie["title"]})

    return friends_unique_movies


def get_available_recs(user_data):
    friend_1 = user_data["friends"][0]["watched"]
    friend_2 = user_data["friends"][1]["watched"]
    subscriptions = user_data["subscriptions"]

    recommendations = []
    for movie in friend_1:
        for service in subscriptions:
            if service == movie["host"]:
                recommendations.append({"title": movie["title"], "host": movie["host"]}) 

    for movie in friend_2:
        for service in subscriptions:
            if service == movie["host"] and movie not in recommendations:
                recommendations.append({"title": movie["title"], "host": movie["host"]})

    return recommendations
        
