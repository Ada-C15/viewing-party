def create_movie(title, genre, rating):
    movie_to_watch = {}
    if title and genre and rating:
        movie_to_watch["title"] = title
        movie_to_watch["genre"] = genre
        movie_to_watch["rating"] = rating
    else:
        return None
    
    return movie_to_watch  

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    
    for i, movie in enumerate(watchlist):
        if movie["title"] == title:
            user_data["watched"].append(movie)
            del watchlist[i]

    # for movie in watchlist:
    #     if movie["title"] == title:
    #         user_data["watched"].append(movie)
    #         watchlist.remove(movie)
    
    return user_data

def get_watched_avg_rating(user_data):
    sum = 0
    avg = 0
    watched = user_data["watched"]

    if len(watched) == 0:
        return avg
    
    for movie in watched:
        sum += movie["rating"]

    avg = sum / len(watched)
    return avg

def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    genre_list = []

    if len(watched) == 0:
        return None

    for movie in watched: 
        genre_list.append(movie["genre"])

    max_genre_count = 0
    most_watched_genre = ""

    genre_count = {}
    for genre in genre_list:
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1
        if genre_count[genre] > max_genre_count:
            max_genre_count = genre_count[genre]
            most_watched_genre = genre

    return most_watched_genre

def get_unique_watched(user_data):
    friends = user_data["friends"]
    friend_watched = set()
    
    for friend in friends:
        for friend_movie in friend["watched"]: 
            friend_watched.add(friend_movie["title"])
                
    
    user_watched = user_data["watched"]
    user_unique_watched = []

    if len(user_watched) == 0:
        return user_unique_watched

    for user_movie in user_watched:
        if user_movie["title"] not in friend_watched:
            user_unique_watched.append(user_movie)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    friends = user_data["friends"]
    friend_watched = []

    for friend in friends:
        for friend_movie in friend["watched"]: 
            friend_watched.append(friend_movie)
    
    user_watched = user_data["watched"]
    friend_unique_watched = []

    if len(friend_watched) == 0:
        return friend_unique_watched
    else:
        for friend_movie in friend_watched:
            if friend_movie not in user_watched and \
                friend_movie not in friend_unique_watched:
                    friend_unique_watched.append(friend_movie)

    return friend_unique_watched

def get_available_recs(user_data):
    user_data_wo_subs = user_data.copy()
    subscriptions = user_data_wo_subs.pop("subscriptions")
    
    user_not_watched = get_friends_unique_watched(user_data_wo_subs)
    available_recs = []
    
    for movie in user_not_watched:
        if movie["host"] in subscriptions:
            available_recs.append(movie)
    
    return available_recs

def get_new_rec_by_genre(user_data):
    user_watched = user_data.copy()
    del user_watched["friends"]
    user_most_watched_genre = get_most_watched_genre(user_watched)
    
    user_likely_watchlist = get_friends_unique_watched(user_data)
    recommended_movie = []

    for movie in user_likely_watchlist:
        if movie["genre"] == user_most_watched_genre:
            recommended_movie.append(movie)
    
    return recommended_movie

def get_rec_from_favorites(user_data):
    user_data_wo_favorites = user_data.copy()
    del user_data_wo_favorites["favorites"]

    friend_likely_watchlist = get_unique_watched(user_data_wo_favorites)
    recommended_movie = []

    for movie in friend_likely_watchlist:
        if movie in user_data["favorites"]:
            recommended_movie.append(movie)
    
    return recommended_movie