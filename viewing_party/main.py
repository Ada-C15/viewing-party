def create_movie(movie_title, genre, rating):
    new_movie = {"title": movie_title, "genre": genre, "rating": rating}
    if movie_title is None or genre is None or rating is None:
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
    if total_rating != 0:
        avg_rating = total_rating/len(user_data["watched"])      
    return avg_rating    

def get_most_watched_genre(user_data):
    genre_frequency_list = []
    for movie in user_data["watched"]: 
        genre_frequency_list.append(movie["genre"])
    if genre_frequency_list == []:
        return None
    return max(set(genre_frequency_list), key=genre_frequency_list.count)
    # alt option: return mode(genre_frequency_list)   #mode() requires "from statistics import mode"

def get_unique_watched(user_data):
    friends_watched_list = []
    user_watched_list = []
    user_unique_watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)
    for movie in user_data["watched"]:
        user_watched_list.append(movie)    
    for movie in user_watched_list:
        if movie not in friends_watched_list:
            user_unique_watched_list.append(movie)
    return user_unique_watched_list

def get_friends_unique_watched(user_data):
    friends_watched_list = []
    user_watched_list = []
    friends_unique_watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)
    for movie in user_data["watched"]:
        user_watched_list.append(movie)    
    for movie in friends_watched_list:
        if movie not in user_watched_list and movie not in friends_unique_watched_list:
            friends_unique_watched_list.append(movie)
    return friends_unique_watched_list


def get_available_recs(user_data):
    subscriptions_list = user_data["subscriptions"]
    recs_list = []
    friends_unique_list = get_friends_unique_watched(user_data)
    for movie in friends_unique_list:
        if movie["host"] in subscriptions_list:
            recs_list.append(movie)
    return(recs_list)


def get_new_rec_by_genre(user_data):
    watched_genre_list = []
    rec_by_genre_list = []
    for movie in user_data["watched"]:
        watched_genre_list.append(movie["genre"])
    if watched_genre_list == []:
        favorite_genre = []
    else:
        favorite_genre = max(set(watched_genre_list), key=watched_genre_list.count)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == favorite_genre:           
                rec_by_genre_list.append(movie)
    return rec_by_genre_list

def get_rec_from_favorites(user_data):
    user_favorite_list = []
    friends_watched_list = []
    recommended_favorites = []
    for movie in user_data["favorites"]:
        user_favorite_list.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)
    for movie in user_favorite_list:
        if movie not in friends_watched_list:
            recommended_favorites.append(movie)        
    return recommended_favorites
        