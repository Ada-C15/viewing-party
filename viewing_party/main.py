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