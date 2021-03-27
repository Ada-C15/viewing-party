def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        movie_dict = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
    return movie_dict

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
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        total = 0
        for movie in user_data["watched"]:
            total += movie["rating"]
        average_rating = total / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None

    popular_genre = {}
    for movie in user_data["watched"]:
        current_genre = movie["genre"]
        popular_genre[current_genre] = popular_genre.get(current_genre, 0) + 1
    
    freq_genre = max(popular_genre)
    return freq_genre

def get_unique_watched(user_data):
    friends_list = []
    for friends_movie in user_data["friends"]:
        for friends_watched in friends_movie["watched"]:
            friends_list.append(friends_watched)
    
    unique_watched_list = []
    for unique_movie in user_data["watched"]:
        if unique_movie not in friends_list:
            unique_watched_list.append(unique_movie)

    return unique_watched_list

def get_friends_unique_watched(user_data):
    unique_movie = []
    for friends_watched in user_data["friends"]:
        for movie in friends_watched["watched"]:
            if movie not in user_data["watched"] and movie not in unique_movie:
                unique_movie.append(movie)

    return unique_movie

def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies

def get_new_rec_by_genre(user_data):
    user_freq_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []

    for movie in friends_unique_movies:
        if movie["genre"] == user_freq_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):
    friends_movie_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_list.append(movie)

    recommended_movies_list = []

    for movie in user_data["favorites"]:
        if movie not in friends_movie_list:
            recommended_movies_list.append(movie)

    return recommended_movies_list




