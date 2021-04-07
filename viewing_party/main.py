def create_movie(title, genre, rating):
    """
    if inputs are truthy, update to dictionary with keys
    that are the name of the parameters
    """
    if (type(title) == str) and (type(genre) == str) and (type(rating) == float):
        library = {"title": title, "genre": genre, "rating": rating}
        return library
    else:
        return None

def add_to_watched(user_data, movie):
    """
    user_data is an empty list of movies 
    movie is a dictionary that is appended to the empty list
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    user_data is an empty list of movies,
    movie is a dictionary that is appended to the empty list
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    user_data is a dictionary with two lists
    function will iteracte through one list and if title is found remove it from
    that list and add it to the second
    """
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

def get_watched_avg_rating(user_data):
    print(user_data["watched"])
    """
    calculate average of all movie rating data provided in input
    """
    total_rating = 0

    if len(user_data["watched"]) == 0:

        return 0.0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]
        avg_rating = total_rating / len(user_data["watched"])
    
    return avg_rating

def get_most_watched_genre(user_data):
    """
    determine most watched genre from list of watched movies
    from input
    """
    movie_genres = {}

    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:
        if movie["genre"] not in movie_genres:
            movie_genres[movie["genre"]] = 1
        else:
            movie_genres[movie["genre"]] += 1
    
    max_watched = max(movie_genres.values())
    for genre, value in movie_genres.items():
        if value == max_watched:
            return genre

def get_unique_watched(user_data):
    friends_not_watched = []
    friend_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie)

    for movie in user_data["watched"]:
        if movie not in friend_watched:
            friends_not_watched.append(movie)

    return friends_not_watched

def get_friends_unique_watched(user_data):
    user_not_watched = []
    user_watched = []

    for movie in user_data["watched"]:
        user_watched.append(movie)
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_watched and movie not in user_not_watched:
                user_not_watched.append(movie)

    return user_not_watched

def get_available_recs(user_data):
    recommended_movies = []

    user_not_watched = get_friends_unique_watched(user_data)
    
    for movie in user_not_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    
    return recommended_movies

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    
    most_watched_genre = get_most_watched_genre(user_data)
    user_not_watched = get_friends_unique_watched(user_data)

    for movie in user_not_watched:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie["title"])
    
    return recommended_movies

def get_rec_from_favorites(user_data):
    pass