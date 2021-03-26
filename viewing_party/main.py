def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None


def add_to_watched(user_data, movie):
    user_data = {
        "watched": [movie]
    }
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie]
    }
    return user_data 


def watch_movie(user_data, title):
    n = 0
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].pop(n)                           
            user_data["watched"].append(movie)
        n += 1
    return user_data


def get_watched_avg_rating(user_data):
    rating_total = 0
    average_rating = 0
    for movie in user_data["watched"]:
        rating_total += movie["rating"]
    if len(user_data["watched"]) > 0:
        average_rating = rating_total / len(user_data["watched"])
    return average_rating


def calculate_genre_frequency(user_data): 
    # returns a dictionary with key as genre and value as genre frequency
    genres = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genres.keys():
            genres[movie["genre"]] += 1
        else:
            genres[movie["genre"]] = 1
    return genres

 
def get_most_watched_genre(user_data):
    # determine which genre has highest frequency, return genre with highest frequency
    # Note: this function doesn't handle a tie in most popular genre
    popular_genre = None
    popular_genre_occurances = 0
    genre_frequency = calculate_genre_frequency(user_data)
    for genre, frequency in genre_frequency.items():
        if frequency > popular_genre_occurances:
            popular_genre = genre
            popular_genre_occurances = frequency
    return popular_genre 


def get_watched_by_friends(user_data):
    # returns a list of dictionaries of movies watched by friends
    watched_by_friends = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in watched_by_friends:
                watched_by_friends.append(movie)
    return watched_by_friends


def get_unique_watched(user_data):
    # returns a list of dictionaries of movies watched by user but not watched by friends
    unwatched_by_friends = []
    watched_by_friends = get_watched_by_friends(user_data)
    for movie in user_data["watched"]:
        if movie not in watched_by_friends:
            unwatched_by_friends.append(movie)
    return unwatched_by_friends


def get_friends_unique_watched(user_data):
    # returns a list of dictionaries of movies watched by a friend but not by user
    unwatched_by_user = []
    watched_by_friends = get_watched_by_friends(user_data)
    for movie in watched_by_friends:
        if movie not in user_data["watched"]:
            unwatched_by_user.append(movie)
    return unwatched_by_user


def get_available_recs(user_data):
    # returns a list of dictionaries of movies that the user has a subscription to 
    # see but that they have not watched although a friend has watched
    available_recs = []
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    return available_recs 


def get_new_rec_by_genre(user_data):
    # returns a list of dictionaries of movies that are in the user's most watched 
    # genre, and that have been watched by a friend but not by the user
    new_rec_by_genre = []
    preferred_genre = get_most_watched_genre(user_data)
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == preferred_genre:
            new_rec_by_genre.append(movie)
    return new_rec_by_genre


def get_rec_from_favorites(user_data):
    # returns a list of dictionaries of movies that are in the user's favorites
    # and have not been seen by any of the user's friends 
    recommended_movies = []
    for movie in get_unique_watched(user_data):
        for favorite in user_data["favorites"]:
            if movie["title"] == favorite["title"]:
                recommended_movies.append(movie)
    return recommended_movies