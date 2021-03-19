# main.py

# --------
# WAVE ONE
# --------

def create_movie(movie_title, genre, rating):
    """
    Creates and returns a movie dictionary. Dictionary contains information
    about the movie.
    """
    if movie_title == None or genre == None or rating == None:
        return None
    movie = {}
    movie['title'] = movie_title
    movie['genre'] = genre
    movie['rating'] = rating
    return movie

def add_to_watched(user_data, movie):
    """
    Adds a movie to the user's watched list.
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    Adds a movie to the user's watchlist.
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    """
    Moves movie from user's watchlist to watched list.
    """
    for movie in user_data['watchlist']:
        if movie['title'] == movie_title:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
            return user_data
    else:
        return user_data


# --------
# WAVE TWO
# --------

def get_watched_avg_rating(user_data):
    """
    Returns the average rating of the movies the user has watched. Works by summing
    the ratings, then dividing by number of movies.
    """
    if len(user_data['watched']) > 0:
        sum = 0
        for movie in user_data['watched']:
            sum += movie['rating']
        return sum / len(user_data['watched'])
    else:
        return 0

def get_most_watched_genre(user_data):
    """
    Returns the most-watched genre in the user's data, or None if no movies in watched
    list. Works by looping through the user data to compile a dictionary of genres the 
    user has watched and how many times each genre has been watched. Determines the most-
    watched genre by finding the maximum value in the dictionary.
    """
    genres = {}

    if len(user_data['watched']) == 0:
        return None

    for movie in user_data['watched']:
        if movie['genre'] in genres:
            genres[movie['genre']] += 1
        else:
            genres[movie['genre']] = 1
    
    max_value = max(genres.values())

    for genre in genres:
        if genres[genre] == max_value:
            return genre


# ----------
# WAVE THREE
# ----------

def get_unique_watched(user_data):
    """
    Returns a list of movies that the user has seen, but the user's friends
    have not seen.
    """
    unique_movies = []
    user_watched_list = user_data['watched']
    friends_watched_list = make_friends_watched_list(user_data)
    for movie in user_watched_list:
        if movie not in friends_watched_list:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    """
    Returns a list of movies that the user's friends have seen, but the user
    has not seen themselves.
    """
    friends_unique_movies = []
    user_watched_list = user_data['watched']
    friends_watched_list = make_friends_watched_list(user_data)
    for movie in friends_watched_list:
        if movie not in user_watched_list:
            friends_unique_movies.append(movie)
    return friends_unique_movies

def make_friends_watched_list(user_data):
    """
    Returns a list of movies that the user's friends have already watched. This list
    will contain each relevant movie title only once. This is a helper function for 
    get_unique_watched() and get_friends_unique_watched(), above.
    """
    friends_watched_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    return friends_watched_list



# ---------
# WAVE FOUR
# ---------

def get_available_recs(user_data):
    """
    Returns a list of movie recommendations that the user has not watched; that have
    been watched by at least one of the user's friends; and that is hosted by a service
    that the user is subscribed to.
    """
    rec_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if (movie['host'] in user_data['subscriptions']) and (movie not in rec_list):
                rec_list.append(movie)
    return rec_list



# ---------
# WAVE FIVE
# ---------

def get_new_rec_by_genre(user_data):
    """
    Returns a list of movie recommendations that fall within the user's most watched
    genre. This list includes movies that at least one of the user's friends have 
    watched, but the user has not yet watched.
    """
    rec_list = []
    favorite_genre = get_most_watched_genre(user_data)
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if (movie not in user_data['watched']) and (len(user_data['watched']) > 0) and (movie['genre'] == favorite_genre):
                if movie not in rec_list:
                    rec_list.append(movie)
    return rec_list

def get_rec_from_favorites(user_data):
    """
    Returns a list of movie recommendations based upon the overlap of the user's favorite
    movies and the movies that none of the user's friends have seen yet.
    """
    rec_list = user_data['favorites']
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie in rec_list:
                rec_list.remove(movie)
    return rec_list
