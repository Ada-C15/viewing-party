def create_movie(movie_title, genre, rating):
    if not movie_title or not genre or not rating:
        return None

    return {"title": movie_title,
            "genre": genre,
            "rating": rating
            }


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            watched_movie = movie
            user_data["watchlist"].remove(watched_movie)
            user_data = add_to_watched(user_data, watched_movie)
            return user_data
    return user_data


def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    ratings = [movie["rating"] for movie in user_data["watched"]]
    return sum(ratings)/len(ratings)


def get_most_watched_genre(user_data):
    # In case of a tie for most watched genre it returns an arbitrary one
    if not user_data["watched"]:
        return None
    genres = [movie["genre"] for movie in user_data["watched"]]
    return max(set(genres), key=genres.count)


def get_unique_watched(user_data):
    friend_watched_titles = set(
        [movie["title"] for friend in user_data["friends"] for movie in friend["watched"]])
    user_unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] not in friend_watched_titles:
            user_unique_movies.append(movie)
    return user_unique_movies


def get_friends_unique_watched(user_data):
    friends_watched_movies = [
        movie for friend in user_data["friends"] for movie in friend["watched"]]
    
    user_watched_titles = [movie["title"] for movie in user_data["watched"]]
    
    friends_unique_watched_titles = []
    friends_unique_watched = []
    
    for movie in friends_watched_movies:
        if movie["title"] not in friends_unique_watched_titles and \
                movie["title"] not in user_watched_titles:
            
            friends_unique_watched_titles.append(movie["title"])
            friends_unique_watched.append(movie)
    
    return friends_unique_watched
