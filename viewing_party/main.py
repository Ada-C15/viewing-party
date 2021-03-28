# <-------------- WAVE 1 ------------------ WAVE 1 ------------------------- >

# test wave 1, part 1:
# create function: create_movie()
# function takes 2 parameters (title, genre, rating)
# IF title, genre and rating == true ==> return a dictionary
# ELSE (title, genre and rating == false ) ==> return None

def create_movie(title, genre, rating):
    movies = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if title and genre and rating:
        print(movies)
        return movies
    else:
        return None

# test wave 1, part 2:
# create function: add_to_watch()
# function takes 2 parameters (user_data, movie)
# user_data ==> dictionary: key = watched; value = []
    # represents that user has NO movies in watched list
# movie ==> dictionary w/ 3 keys: title, genre, rating
# add movie to watched list inside of user_data
# return user_data

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# test wave 1, part 3:
# SAME AS PART 2, DIFF VARIABLES

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# test wave 1, part 4:
# create function watch_movie
# function takes 2 parameters: user_data, title
# user_data ==> dictionary: key: watchlist, watched; value: []
# title ==> string (title of movie user has watched)
# IF title of movie is IN user's watchlist:
    # remove movie from WATCHLIST
    # ADD movie to WATCHED
    # return user_data
# IF title of movie IS NOT IN user's watchlist:
    # return user_data
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data


# <-------------- WAVE 2 ------------------ WAVE 2 ------------------------- >

# test wave 2, part 1:
# create function get_watched_avg_rating, function takes 1 parameter: user_data
# need to: access "rating"
# iterate through "rating"
# append value of "rating" into empty list
# calculate average value of rating_list
# return the average rating

def get_watched_avg_rating(user_data):
    ratings = []
    for watched, movies in user_data.items():
        for movie_details in movies:
            ratings.append([movie_details][0]["rating"])

    if len(ratings) == 0:
        return 0.0
    else:
        ratings_avg = (sum(ratings) / len(ratings))
        return ratings_avg

# test wave 2, part 2:
# create function get_most_watched_genre, function takes 1 parameter: user_data
# need to access "genre"
# determine which genre is frequently occuring in the watched list
# return genre that is most frequently watched

def get_most_watched_genre(user_data):
    genre = []
    for watched, movies in user_data.items():
        for movie_details in movies:
            genre.append([movie_details][0]["genre"])

    genre_frequency = {}
    for type in genre:
        if type not in genre_frequency:
            genre_frequency[type] = 1
        else:
            genre_frequency[type] += 1

    if user_data["watched"] == []:
        return None
    else:
        common_genre = max(genre_frequency, key=genre_frequency.get)
        return common_genre


# <-------------- WAVE 3 ------------------ WAVE 3 ------------------------- >

# test wave 3, part 1:
# create function get_unique_watched, function takes 1 parameter: user_data
# determine which movies the user has watched but NONE of their friends has watched
# add list of movies of movies to unique movies list
# return unique movies

def get_unique_watched(user_data):
    unique_movies = []
    friends_movies = []

    if not user_data["watched"]:
        return []

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            friends_movies.append(movie)

    for each_movie in user_data["watched"]:
        if each_movie not in friends_movies:
            unique_movies.append(each_movie)

    return unique_movies

# test wave 3, part 2:
# create function get_friends_unique_watched, function takes 1 parameter: user_data
# consider the movies the user has watched and the movies their friends have watched
# determine which movies the user's friends have watched BUT the user hasn't
# return list of dictionary ==> movies that the user hasn't watched
# similar to part 1 but the reverse reverse!!!

def get_friends_unique_watched(user_data):
    user_movies = []
    friends_movies = []
    friends_unique = []

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if movie not in user_data["watched"]:
                friends_movies.append(movie)

    if (len(user_data["watched"])) == 0:
        for friends in user_data["friends"]:
            for movie in friends["watched"]:
                friends_movies.append(movie)

    friends_unique_pt2 = []
    for i in range(len(friends_movies)):
        if friends_movies[i] not in friends_movies[i + 1:]:
            friends_unique_pt2.append(friends_movies[i])

    return friends_unique_pt2

# <-------------- WAVE 4 ------------------ WAVE 4 ------------------------- >

# create a function named get_available_recs, function takes 1 parameter: user_data
# determine a LIST (with nested dict) of recommended movies
# movie should be added to the list IF AND ONLY IF:
# user has not watched it 
# at least one of the user's friends has watched
# host of the movie is a service that is in the user's subscriptions
# return list of recommended movies

def get_available_recs(user_data):

    friends_host = []
    user_host = (user_data["subscriptions"])

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if movie["host"] in user_host:
                friends_host.append(movie)

    friends_host_pt2 = []
    for i in range(len(friends_host)):
        if friends_host[i] not in friends_host[i + 1:]:
            friends_host_pt2.append(friends_host[i])

    return friends_host_pt2

# <-------------- WAVE 5 ------------------ WAVE 5 ------------------------- >

# test wave 5, part 1:
# create a function get_new_rec_by_genre, function takes 1 parameter: user_data
# consider the user's most frequently watched genre THEN determine a list of recommended movies
# movie should only be added to recommended movies list IF AND ONLY IF:
# the user has not watched it
# at least one of the user's friends has watched
# genre of the movie == user's most frequent genre
# return list of recommended movies

def get_new_rec_by_genre(user_data):
    recommended_movies = []

# append user's watched titles into new list
    user_titles = []
    for details in user_data["watched"]:
        user_titles.append(details["title"])

# append user's genre into new list
    user_genre = []
    for details in user_data["watched"]:
        user_genre.append(details["genre"])

# create dictionary to determine user's msot frequent genre type
    user_genre_frequency = {}
    for type in user_genre:
        if type not in user_genre_frequency:
            user_genre_frequency[type] = 1
        else:
            user_genre_frequency[type] += 1

# create variable for user's favorite genre & condition if user's watched data is empty
    if user_data["watched"] == []:
        return []
    else:
        user_fav_genre = max(user_genre_frequency, key=user_genre_frequency.get)

# iterate through friends watched list. Append ONLY if genre == user_fav_genre AND title is NOT IN user_titles
    for friends in user_data["friends"]:
        for movies in friends["watched"]:
            if movies["genre"] in user_fav_genre and movies["title"] not in user_titles:
                recommended_movies.append(movies)


# print(user_titles)
# print(user_genre)
# print(user_genre_frequency)
# print(user_fav_genre)
    return recommended_movies
    # print(recommended_movies)


# test wave 5, part 2:
# create a function get_rec_from_favorites, function takes 1 parameter: user_data
# determine a list of recommended movies
# movie should only be added to recommended movies IF AND ONLY IF:
# movie is in user's favorites
# none of the user's friends have watched it
# return list of recommended movies 

def get_rec_from_favorites(user_data):
    favorite_movies = []

# append user's favorites to new list
    user_favorites = []
    for details in user_data["favorites"]:
        user_favorites.append(details)

    user_watched = []
    for titles in user_data["watched"]:
        user_watched.append(titles)

    friends_watched = []
    for friends in user_data["friends"]:
        for movies in friends["watched"]:
            friends_watched.append(movies)

    unique_faves = []
    for title in user_watched:
        if title not in friends_watched:
            unique_faves.append(title)

    return unique_faves