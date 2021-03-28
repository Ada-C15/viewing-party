def create_movie(movie_title, genre, rating):
    new_movie = {
        "title": movie_title, 
        "genre": genre, 
        "rating": rating
        }
    if not (movie_title and genre and rating):
        return None 
    else:  
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, name):
    for movie in user_data["watchlist"]:
        if movie["title"] == name:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

def get_watched_avg_rating(user_data):
    total_rating = 0
    avg_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    if len(user_data["watched"]) != 0:
        avg_rating = total_rating/len(user_data["watched"])      
    return avg_rating    

def get_most_watched_genre(user_data):
    genre_frequency_dict = {}
    for movie in user_data["watched"]: 
        if movie["genre"] not in genre_frequency_dict:   
            genre_frequency_dict[movie["genre"]] = 1 
        else:
            genre_frequency_dict[movie["genre"]] += 1 
    if genre_frequency_dict == {}:
        return None
    return max(genre_frequency_dict, key=genre_frequency_dict.get)    

def get_unique_watched(user_data):
    friends_watched_list = []
    user_unique_watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)
    for movie in user_data["watched"]:
        if movie not in friends_watched_list:
            user_unique_watched_list.append(movie)
    return user_unique_watched_list

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friends_unique_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
           if movie not in user_watched_list and movie not in friends_unique_watched_list:
               friends_unique_watched_list.append(movie)   
    return friends_unique_watched_list

def get_available_recs(user_data):
    friends_unique_list = get_friends_unique_watched(user_data)
    recs_list = [movie for movie in friends_unique_list if movie["host"] in user_data["subscriptions"]]
    return(recs_list)

def get_new_rec_by_genre(user_data):
    watched_genre_dict = {}
    rec_movie_list = []
    for movie in user_data["watched"]:
        if movie["genre"] not in watched_genre_dict:
            watched_genre_dict[movie["genre"]] = 1
        else:
            watched_genre_dict[movie["genre"]] += 1 
    if watched_genre_dict == {}:
        return rec_movie_list
    else:    
        user_fav_genre = max(watched_genre_dict, key=watched_genre_dict.get)
    for friend in user_data["friends"]:  
        for movie in friend["watched"]:
            if movie["genre"] == user_fav_genre:
                rec_movie_list.append(movie) 
    return rec_movie_list

def get_rec_from_favorites(user_data):
    friends_watched_list = [movie for friends in user_data["friends"] for movie in friends["watched"]]
    recommended_favorites = [movie for movie in user_data["favorites"] if movie not in friends_watched_list]
    return recommended_favorites
