
def create_movie(title, genre, rating):
    """
    This function returns a dictionary of movies using the passed parameters as keys. It will return "None" if any parameter is empty.
    """
    movie_library = {}
    if title and genre and rating:
        movie_library ={
                        "title": title,
                        "genre": genre,
                        "rating": rating,
                }
        return movie_library
    else:
        return None

def add_to_watched(user_data, movie):
    """
    This function appends the passed movie argument to a "watched" list that is nested in user_data
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    This function appends the passed movie argument to a "watchlist" list that is nested in user_data
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    This function removes the passed argument "title" from the nested list "watchlist" and appends it to the nested list "watched". If "title" is not on the user's watchlist, the function returns user_data unchaged  
    """
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

def get_watched_avg_rating(user_data):
    """
    This function accepts user_data and returns the average rating of all movies in the user's nested list "watched". If there are no ratings the function returns 0.0
    """
    user_ratings = []
    for movie in user_data["watched"]:
        user_ratings.append(movie["rating"])
    if len(user_ratings) == 0:
        return 0.0
    else:
        average_rating = sum(user_ratings)/len(user_ratings)
    return average_rating
        
def get_most_watched_genre(user_data):
    """
    This function returns the genre with the most occurances in the user's nested "watched" list. If there is no genre information the function returns "None"
    """
    watched_genres = []
    for movie in user_data["watched"]:
        watched_genres.append(movie["genre"])
    if len(watched_genres) == 0:
        return None
    else:
        genre_count = {}
        for genre in watched_genres:
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
        return max(genre_count, key = genre_count.get)

def get_unique_watched(user_data):
    """
    This function returns a list of dictionaries representing movies that the user has watched and the user's friends have not watched
    """
    # initialize empty lists for user and friends watched movies
    unique_user_watched = []
    friends_watched = []

    # append all movies friends watched to friends_watched
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_watched.append(friend_movie)

    # append all movies the user has watched, but friends have not watched to unique_user_watched
    for user_movie in user_data["watched"]:
        if user_movie not in friends_watched:
            unique_user_watched.append(user_movie)

    # return a list of dictionaries that represents a list of movies
    return unique_user_watched 

def get_friends_unique_watched(user_data):
    """This function returns a list of dictionaries representing movies watched by at least one of the user's friends that the user has not watched
    """
    # initialize empty lists
    user_watched = []
    temp = []
    friends_unique_watched = []

    # collect a list of movies that the user has watched
    for user_movie in user_data["watched"]:
        user_watched.append(user_movie)

    # collect a list of movies the user's friends have watched
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_watched:
                temp.append(friend_movie)

    # remove duplicate movies
    for i in range(len(temp)):
        if temp[i] not in friends_unique_watched:
            friends_unique_watched.append(temp[i])
    
    # return a list of dictionaries that represents a list of movies
    return friends_unique_watched

def get_available_recs(user_data):
    """
    This function returns a list of dictionaries representing movies watched by at least one of the user's friends AND that the user has not watched AND that are hosted by one of the user's subscription services  
    """
    # use helper function to get movies watched by friends and not by user
    friends_unique_watched = get_friends_unique_watched(user_data)
    # initialize empty lists
    availible_recs = []
    user_subscription = []

    # build a list of user subscription services 
    for subscription in user_data["subscriptions"]:
        user_subscription.append(subscription)

    # build a list of movies that the user has not watched AND at least one friend has watched AND hosted by users subscription providers
    for movie in friends_unique_watched:   
        for value in movie.values():
            if value in user_subscription:
                availible_recs.append(movie)
    
    # return list of recommended movies
    return availible_recs

def get_new_rec_by_genre(user_data):
    """
    This function returns a list of dictionaries representing movies watchd by at least one of the user's friends AND not watched by the user AND in the user's most watched genre category
    """
    # use helper functions
    user_most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    # initialize empty lists
    rec_by_genre = []
    # append movies watched by friends in the user's most genre to a list
    for movie_rec in friends_unique_watched:
        for value in movie_rec.values():
            if value == user_most_watched_genre:
                rec_by_genre.append(movie_rec)
    # return list of dictionaries
    return rec_by_genre

def get_rec_from_favorites(user_data):
    """
    This function returns a list of dictionaries representing movies not watched by any of the user's friends AND from the user's "favorites" list
    """
    # initialize empty lists
    friends_watched = []
    favorite_recs = []
    # create a list of movies watched by friends 
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_watched.append(friend_movie)
    # compare user's favorite movies to friends watched list
    for favorite in user_data["favorites"]:
        if favorite not in friends_watched:
            favorite_recs.append(favorite)
    # return list of dictionaries
    return favorite_recs