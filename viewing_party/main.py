# WAVE 1

def create_movie(title, genre, rating):

    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]

    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            user_data["watched"].append(movie)

    return user_data


# WAVE 2

def get_watched_avg_rating(user_data):

    sum = 0

    for watched_movies, movie_info in user_data.items():

        if not movie_info:
            avg = 0.0
        else:
            for movie in movie_info:
                sum += movie["rating"]
            avg = sum / len(user_data["watched"])

    return avg


def get_most_watched_genre(user_data):
    
    genre_count = {}

    most_popular_genre = {
    "genre": 0,
    "count": 0
    }

    for watched_movies, movie_info in user_data.items():
        
        if not movie_info:
            return None
        else:
            for movie in movie_info:
                if movie["genre"] not in genre_count:
                    genre_count[movie["genre"]] = 1
                elif movie["genre"] in genre_count:
                    genre_count[movie["genre"]] += 1
            for genre, count in genre_count.items():
                if count > most_popular_genre["count"]:
                    most_popular_genre["count"] = count
                    most_popular_genre["genre"] = genre

            return most_popular_genre["genre"]


# WAVE 3

def get_unique_watched(user_data):

    unique_watched_movies = []
    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movies.append(movie)
    
    for movie in user_data["watched"]:
        if movie not in friends_watched_movies:
            unique_watched_movies.append(movie)
    
    return unique_watched_movies


def get_friends_unique_watched(user_data):

    users_unwatched_movies = []
    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)
    
    for movie in friends_watched_movies:
        if movie not in user_data["watched"]:
            users_unwatched_movies.append(movie)
    
    return users_unwatched_movies


# WAVE 4

def get_available_recs(user_data):

    recommended_movies = []
    users_unwatched_movies = []
    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)
    
    for movie in friends_watched_movies:
        if movie not in user_data["watched"]:
            users_unwatched_movies.append(movie)

    for movie in users_unwatched_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies


# WAVE 5

def get_new_rec_by_genre(user_data):

    genre_count = {}
    times_watched = 0
    favorite_genre = {}

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        elif movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1

    for genre in genre_count:
        if genre_count[genre] > times_watched:
            times_watched = genre_count[genre]
            favorite_genre = genre

    users_unwatched_movies = []
    friends_watched_movies = []
    recommended_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)

    for movie in friends_watched_movies:
        if movie not in user_data["watched"]:
            users_unwatched_movies.append(movie)

    for movie in users_unwatched_movies:
        if favorite_genre == movie["genre"]:
            recommended_list.append(movie)

    return recommended_list


def get_rec_from_favorites(user_data):

    unique_favorite_movies = []
    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movies.append(movie)
    
    for movie in user_data["favorites"]:
        if movie not in friends_watched_movies:
            unique_favorite_movies.append(movie)
    
    return unique_favorite_movies















