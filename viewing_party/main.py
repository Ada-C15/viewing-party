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
    for x in range(len(user_data["watchlist"])):
        if user_data["watchlist"][x]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][x])
            user_data["watchlist"].pop(x)
    return user_data