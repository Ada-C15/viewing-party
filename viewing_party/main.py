
def create_movie(movie_title,genre,rating):
    movie = {}
    if movie_title == None or genre == None or rating == None:
        return None
    else: 
        movie["title"] = movie_title
        movie["genre"] = genre
        movie["rating"] = rating
    print(movie)
    return movie

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return(user_data)

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return(user_data)

def watch_movie(user_data, movie):
    for elem in user_data['watchlist']:
        if movie == elem['title']:
            user_data['watchlist'].remove(elem)
            user_data['watched'].append(elem)
    return user_data 