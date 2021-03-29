def create_movie(movie_title, genre, rating): 
    if movie_title == None or genre == None or rating == None:
        new_movie = None
    else:
        new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
        }
    
    return new_movie

def add_to_watched(user_data, movie): 
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie): 
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title): 
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
            
    return user_data

def get_watched_avg_rating(user_data): 
    ratings = []
    average = 0
    
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
        average = sum(ratings) / len(ratings)

    return average

def get_most_watched_genre(user_data): 
    genres = dict()
    # for every movie in the user's "watched" list,
    # into the empty dictionary "genres", create a key == to a type of genre
    # and assign a value to each individual key that keeps a count of how many 
    # times the key is found in the list
    for movie in user_data["watched"]:
        genres[movie["genre"]] = genres.get(movie["genre"], 0) + 1
    
    if not genres:
        return None 

    return (max(genres))
    
def get_unique_watched(user_data): 
    user_set = {movie["title"] for movie in user_data["watched"]}

    friend_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_set.add(movie["title"])

    unique_set = user_set - friend_set  

    unique_titles = [{"title": title} for title in unique_set]
    
    return unique_titles

def get_friends_unique_watched(user_data): 
    user_set = {movie["title"] for movie in user_data["watched"]}
    
    friends_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_set.add(movie["title"])

    friends_unique_movies = [{"title": movie} for movie in friends_set if movie not in user_set]
    
    return friends_unique_movies

def get_available_recs(user_data): 
    friends_watched = []
    for friend in user_data["friends"]:
        for entry in friend["watched"]:
            friends_watched.append(entry)

    for movie in friends_watched:
        if friends_watched.count(movie) > 1:
            friends_watched.remove(movie)

    recommendations = [movie for movie in friends_watched if movie["host"] in \
        user_data["subscriptions"]]
    
    return recommendations
    
def get_new_rec_by_genre(user_data): 
    most_popular = get_most_watched_genre(user_data)
    
    user_watched = [movie for movie in user_data["watched"]]
    
    friends_watched = []
    for friend in user_data["friends"]:
        for entry in friend["watched"]:
            friends_watched.append(entry)

    recommendations = [movie for movie in friends_watched \
        if movie not in user_watched and movie["genre"] == most_popular]

    return recommendations 

def get_rec_from_favorites(user_data): 
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    recommendations = [movie for movie in user_data["favorites"]\
        if movie not in friends_watched]
    
    return recommendations

    
        
