# wave_01 
def create_movie(movie_title, genre, rating): 
    new_movie = {
                "title": movie_title,
                "genre": genre,
                "rating": rating         
                }
    for value in new_movie.values(): 
        if value == None:
            new_movie = None
        
    return new_movie

def add_to_watched(user_data, movie): 
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie): 
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]: 
        if movie["title"] == title: 
            user_data["watchlist"].remove(movie) 
            user_data["watched"].append(movie) 
    
    return user_data

# wave_02 
def get_watched_avg_rating(user_data): 
    total_rating = 0.0
    average_rating = 0.0
    watched_movie_amount = 0

    for movie in user_data["watched"]: 
        total_rating += movie["rating"]
        watched_movie_amount += 1
    
    if watched_movie_amount > 0: 
        average_rating = total_rating / watched_movie_amount
    else: 
        average_rating == 0.0
    
    return average_rating

def get_most_watched_genre(user_data): 
    watched_genre_counts ={} 
    popular_genre = None

    for movie in user_data["watched"]: 
        if movie["genre"] not in watched_genre_counts: 
            watched_genre_counts[movie["genre"]] = 1 
        else: 
            watched_genre_counts[movie["genre"]] += 1

    for genre, count in watched_genre_counts.items(): 
        max_genre_count = max(watched_genre_counts.values())
        if count == max_genre_count:
            popular_genre = genre 
    
    return popular_genre

# wave_03
def get_user_most_watched(user_data): 
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
    return user_watched

def get_friends_most_watched(user_data): 
    friends_watched =[]
    for friend in user_data["friends"]: 
        for movie in friend["watched"]: 
            friends_watched.append(movie)
    
    return friends_watched

# a function call that gets user watched movies and gets friends watched movie, and return
# the movies that are watched by user but not their friends 
def get_unique_watched(user_data): 
    user_watched = get_user_most_watched(user_data)  
    friends_watched = get_friends_most_watched(user_data)
    unique_user_watched = []
    
    for movie in user_watched: 
        if movie not in friends_watched and movie not in unique_user_watched:
            unique_user_watched.append(movie)
    return unique_user_watched

# a function call that gets user watched movies and gets friends watched movie, and return
# the movies that are watched by friends but not the user    
def get_friends_unique_watched(user_data): 
    user_watched = get_user_most_watched(user_data)  
    friends_watched = get_friends_most_watched(user_data)
    unique_friends_watched = []
    
    for movie in friends_watched: 
        if movie not in user_watched and movie not in unique_friends_watched: 
            unique_friends_watched.append(movie)
    return unique_friends_watched

# wave_04
def get_available_recs(user_data): 
    unique_friends_watched = get_friends_unique_watched(user_data)
    movie_recs = []

    for movie in unique_friends_watched: 
        if movie["host"] in user_data["subscriptions"] and movie["title"] not in movie_recs: 
            movie_recs.append(movie) 
    
    return movie_recs

# wave_05
def get_new_rec_by_genre(user_data):
    unique_friends_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    movie_recs_by_genre =[]

    for movie in unique_friends_watched:
        if movie["genre"] is most_watched_genre and movie not in movie_recs_by_genre:
            movie_recs_by_genre.append(movie)
    
    return movie_recs_by_genre

def get_rec_from_favorites(user_data): 
    unique_user_watched = get_unique_watched(user_data)
    movie_recs_from_favorites = []

    for movie in user_data["favorites"]: 
        if movie in unique_user_watched and movie not in movie_recs_from_favorites: 
            movie_recs_from_favorites.append(movie)
    
    return movie_recs_from_favorites
    


    

