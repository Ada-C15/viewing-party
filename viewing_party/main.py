# WAVE 1 *****************************************************************

# create a dictionary from data title, genre, rating
def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None

# add watched movie to watched list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# add movie to list of movies to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data 

# remove movie from watchlist and move to watched 
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title: # if title is found in watchlist and watched list
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data 

# WAVE 2 *****************************************************************

# get average rating of movie
def get_watched_avg_rating(user_data):
    sum = 0
    avg_rating = 0.0

    if len(user_data["watched"]) == 0:
        return avg_rating

    for movie in user_data["watched"]:
        sum = sum + movie["rating"]

    avg_rating = sum / len(user_data["watched"])
    return avg_rating

# get genre that user most watched 
def get_most_watched_genre(user_data):
    most_watched_genre = {}

    for movie in user_data["watched"]:
        if movie["genre"] in most_watched_genre:
            most_watched_genre[movie["genre"]] += 1
        else:
            most_watched_genre[movie["genre"]] = 1

    max = 0
    max_genre = None

    for genre, count in most_watched_genre.items():
        if count > max:
            max = count 
            max_genre = genre  
    return max_genre

# WAVE 3 *****************************************************************

# find movies the user has watched but friends have not seen
def make_friends_list(user_data):
    friends_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_list.append(movie)
    return friends_list
    
def get_unique_watched(user_data):
    friends_list = make_friends_list(user_data)
    user_list = []
    for user_movie in user_data["watched"]:
        if user_movie not in friends_list:
            user_list.append(user_movie)
    return user_list



# Determine which movies at least one of the user's friends have watched, but the user has not watched.
def get_friends_unique_watched(user_data):
    friends_list = make_friends_list(user_data)
    user_unwatched = []
    for friend_movie in friends_list:
        if (friend_movie not in user_data["watched"] 
        and friend_movie not in user_unwatched):
            user_unwatched.append(friend_movie)
    return user_unwatched



# WAVE 4 ***************************************************************

# Get list of reccommended movies that user hasn't watch, friends have watch and are in users subscriptions
def get_available_recs(user_data):
    
    recommended_movies = []

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if (friend_movie["host"] in user_data["subscriptions"]
            and friend_movie not in user_data["watched"] 
            and friend_movie not in recommended_movies):
                recommended_movies.append(friend_movie)
    return recommended_movies


# WAVE 5 ***************************************************************

# Get reccomended movies by genre
def get_new_rec_by_genre(user_data):

    recommended_movies = []
    fav_genre = get_most_watched_genre(user_data)

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["genre"] == fav_genre and friend_movie \
                not in user_data["watched"] and friend_movie not in recommended_movies:
                recommended_movies.append(friend_movie)
    return recommended_movies

# Get user reccomended favorite movies that their friends haven't watched
def get_rec_from_favorites(user_data):
    
    recommended_movies = user_data['favorites']

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie in user_data['favorites']:
                recommended_movies.remove(friend_movie)
    return recommended_movies
        