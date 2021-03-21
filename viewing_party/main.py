def create_movie(title, genre, rating):
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched": []
    }
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": []
    }
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for k,v in user_data.items():
        # k: watchlist, v: [...] (2)
        # k: watched, v: [...] (1)
        if k == "watchlist":
            for movie in v: # initial length: 2
                if movie["title"] == title:
                    user_data["watchlist"].remove(movie)
                    user_data["watched"].append(movie)
                    return user_data
            # return use_data
        # return use_data

    return user_data



