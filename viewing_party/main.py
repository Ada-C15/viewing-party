movie_dict = {} 
user_data = {}
#user_data = {"watched":[{movie},{},{}...],
#              "watchlist":[{movie},{},{}...],
#              "friends":[{friend},{},{}...],
#              "subscriptions": ["string","",""]
#              "favorites": [{movie},{},{}...]}
#{movie} --> {"title":"string" , "genre":"string" , "rating":float}
#{friend} --> {"watched": [{movie2},{},{}...]}
#{movie2} --> {"title":"string" , "host": "streaming"}


#Wave 1 
#Q1 - add a new movie(title,genre,rating) to movie_dict
def create_movie(title,genre,rating):
    if not title or not genre or not rating:
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

#Q2 - add a movie to list "watched"
def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

#Q3 - add a movie to list "watchlist"
def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

#Q4 - move a movie from "watchlist" to "watched" if in watched list, otherwisde return user_data
def watch_movie(user_data,title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if title in movie["title"]:
            watchlist.remove(movie)
            watched.append(movie)
            return user_data
    else:
        return user_data


#Wave 2: 
#Q1 - Avg rating of watched
def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if len(ratings) == 0:
        avg_ratings = 0 
    else:    
        avg_ratings = sum(ratings)/len(ratings)
    return avg_ratings

#Q2 - Most watched genere 
def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0: 
        return None
    else:
        genres = []
        for movie in user_data["watched"]:
            genres.append(movie["genre"])
        genres_count = {}
        for genre in genres:
            if genre in genres_count:
                genres_count[genre] +=1
            else:
                genres_count[genre] =1
        fav_genre = max(genres_count, key=genres_count.get)
        return fav_genre


#Wave 3:
#Q1 - A list of movies user has watched but friends haven't
def get_unique_watched(user_data):
    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)    
    user_unique_movies = []
    for movie in user_data["watched"]:
        if movie not in friends_movies:
            user_unique_movies.append(movie)
    return user_unique_movies

#Q2 - A list of movies friends have watched but the user hasn't
def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movies:
               friends_unique_movies.append(movie)
    return friends_unique_movies
    

#Wave 4:
# Recommend list - friends watched, user hasn't watched, user has subscriptions
def get_available_recs(user_data):
    unique_movies = get_friends_unique_watched(user_data)
    recommend_movies = []
    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"] and movie not in recommend_movies:
            recommend_movies.append(movie)
    return recommend_movies


#Wave 5:
#Q1 - Recommend list - friends watched, user hasn't watched, user's fav genre
def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    unique_movies = get_friends_unique_watched(user_data)
    recommend_movie = []
    for movie in unique_movies:
        if movie["genre"] == fav_genre:
            recommend_movie.append(movie)
    return recommend_movie

#Q2 - Recommend list = in user's favorites, friends have not watched 
def get_rec_from_favorites(user_data):
    user_unique_movies = get_unique_watched(user_data)
    recommend_movies = []
    for movie in user_unique_movies:
        if movie in user_data["favorites"]:
            recommend_movies.append(movie)
    return recommend_movies