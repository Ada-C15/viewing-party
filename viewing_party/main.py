def create_movie(movie_title, genre, rating):
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }
    if movie_title and genre and rating:
        return new_movie
    return None

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

def get_watched_avg_rating(user_data):
    total = 0
    for movie in user_data["watched"]:
        total += movie["rating"]
    if len(user_data["watched"]) > 0:
        average = total/len(user_data["watched"])
    else:
        return 0.0
    return average

def get_most_watched_genre(user_data):
    most_watched_genre = {}
    popular_genre = None
    for movie in user_data["watched"]:
        if movie["genre"] not in most_watched_genre:
            most_watched_genre[movie["genre"]] = 1
        else:
            most_watched_genre[movie["genre"]] += 1
        popular_genre = max(most_watched_genre, key = most_watched_genre.get)
    return popular_genre

def get_unique_watched(user_data):
    users_unique_movies = []
    friends_watched = []
    for movies_friends_watched in user_data["friends"]:
        for each_movie in movies_friends_watched["watched"]:
            friends_watched.append(each_movie)
    for movies_user_watched in user_data["watched"]:
        if movies_user_watched not in friends_watched:
            users_unique_movies.append(movies_user_watched)
    return users_unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friends_watched = []
    user_watched = []
    for movies_user_watched in user_data["watched"]:
        user_watched.append(movies_user_watched)
    for movies_friends_watched in user_data["friends"]:
        for each_movie in movies_friends_watched["watched"]:
            if each_movie not in user_watched and each_movie not in friends_unique_movies:
                friends_unique_movies.append(each_movie)
    return friends_unique_movies

def get_available_recs(user_data):
    recommendations = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie_recs in friends_unique_movies:
        if movie_recs["host"] in user_data["subscriptions"]:
            recommendations.append(movie_recs)
    return recommendations

def get_new_rec_by_genre(user_data):
    recommendations = []
    users_frequently_watched_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie_recs in friends_unique_movies:
        if movie_recs["genre"] == users_frequently_watched_genre and movie_recs in friends_unique_movies:
            recommendations.append(movie_recs)
    return recommendations
    
def get_rec_from_favorites(user_data):
    recommendations = []
    users_unique_movies = get_unique_watched(user_data)
    for favorites in user_data["favorites"]:
        if favorites in users_unique_movies:
            recommendations.append(favorites)
    return recommendations
