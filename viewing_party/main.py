

def create_movie(title, genre, rating):
    movie_dictionary = {
        "title": title, 
        "genre": genre, 
        "rating": rating
        } 
    if not title == None and not genre == None and not rating == None:
        return movie_dictionary
    else:
        return None 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie) 
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    list_of_watched_movies = user_data["watched"]
    watch_list = user_data["watchlist"]
    
    for i in range (len(watch_list)):
        title_of_watchlist_movie = user_data["watchlist"][i]["title"]
        if title == title_of_watchlist_movie:
            list_of_watched_movies.append(watch_list.pop(i))
    return user_data
    
def get_watched_avg_rating(user_data):  
    total = 0
    average = 0.0
    if len(user_data["watched"]) == 0:
        average = 0.0
    else:
        for movie in user_data["watched"]:
            total += movie["rating"]
        average = total / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    list_of_movies = user_data["watched"]
    
    if not list_of_movies:
        return None
    
    else:
        list_of_genres = [] 
        count = 0
        most_pop_genre = ""
        
        for movie in list_of_movies:
            list_of_genres.append(movie["genre"])
            for genre in list_of_genres:
                frequency = list_of_genres.count(genre)
                if frequency > count:
                    count = frequency
                    most_pop_genre = genre

        return most_pop_genre

def get_unique_watched(user_data):
    user_watched_list_of_dicts = user_data["watched"]
    friend_watched_list_of_dicts = user_data["friends"]
    
    unique_watched_list = []
    user_watched_list = []
    friends_watched_list = []
    
    for movie in user_watched_list_of_dicts:
        user_watched_list.append(movie)
    
    for friend_info in friend_watched_list_of_dicts:
        for movie in friend_info["watched"]:
            friends_watched_list.append(movie)
    for movie in user_watched_list:
        if not movie in friends_watched_list and not movie in unique_watched_list:
            unique_watched_list.append(movie)

    return unique_watched_list

def get_friends_unique_watched(user_data):
    user_watched_list_of_dicts = user_data["watched"]
    friend_watched_list_of_dicts = user_data["friends"]
    
    unique_watched_list = []
    user_watched_list = []
    friends_watched_list = []

    for movie in user_watched_list_of_dicts:
        user_watched_list.append(movie)
    for friend_info in friend_watched_list_of_dicts:
        for movie in friend_info["watched"]:
            friends_watched_list.append(movie)
    
    for film in friends_watched_list:
            if film in friends_watched_list and film not in user_watched_list and film not in unique_watched_list:
                unique_watched_list.append(film)
    return unique_watched_list

def get_available_recs(user_data):
    recommended_movies = [] 
    services_avail = user_data["subscriptions"]
    list_of_friends = user_data["friends"]

    for friend in list_of_friends:
        for watched, details in friend.items():
            for movie in details:
                if movie["host"] in services_avail:
                    if movie not in user_data["watched"] and movie not in recommended_movies:
                        recommended_movies.append(movie)
    return recommended_movies
                    
def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    user_friend_watch = get_friends_unique_watched(user_data)

    recommended_movies = []
    for movie in user_friend_watch:
        if movie["genre"] == fav_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    no_friends_watched = get_unique_watched(user_data)
    favorites = user_data["favorites"]
    recommended_movies = []

    for movie in no_friends_watched:
        if movie in favorites:
            recommended_movies.append(movie)

    return recommended_movies