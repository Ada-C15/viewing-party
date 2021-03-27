def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        return { "title" : title,
        "genre" : genre,
        "rating" : rating }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data     

#wave 2

def get_watched_avg_rating(user_data): 
    if not user_data["watched"]: 
        return 0
    total = 0 
    for movie in user_data["watched"]:
        total += movie["rating"]
    return total/ (len(user_data["watched"]))


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None 

    freq_map = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in freq_map:
            freq_map[genre] += 1
        else:
            freq_map[genre] = 1
    popular_genre = max(freq_map) 
    return popular_genre


def get_unique_watched(user_data):
    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]: 
            friends_movies.append(movie) 

    unique_watched = []
    for movie in user_data["watched"]:
        if movie not in friends_movies: 
            unique_watched.append(movie) 

    return unique_watched
    

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie\
                not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies



def get_available_recs(user_data): 
    friends_unique = get_friends_unique_watched(user_data) 
    recommended_movies = [] 
    for movie in friends_unique: 
        if movie["host"] in user_data["subscriptions"]: 
            recommended_movies.append(movie)

    return recommended_movies


def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)  
    friend_unique = get_friends_unique_watched(user_data)
    rec_by_genre = []
    for movie in friend_unique:
        if movie["genre"] == most_watched_genre:
            rec_by_genre.append(movie)

    return rec_by_genre

def get_rec_from_favorites(user_data):
    recommended = []
    unique_watched = get_unique_watched(user_data)
    for movie in unique_watched:
        if movie in user_data["favorites"]:
            recommended.append(movie)

    return recommended
