def create_movie(movie_title, genre, rating):
    new_movie = {"title": movie_title, "genre": genre, "rating": rating}
    if movie_title is None or genre is None or rating is None:
        return None 
    else:  
        return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, name):
    for movie in user_data["watchlist"]:
        if movie["title"] == name:
            a = user_data["watchlist"].pop(movie)
            user_data["watched"][0] = a
            return user_data
