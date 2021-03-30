def create_movie(title, genre, rating):
    movies_dict = {}
    if title and genre and rating:
        movies_dict["title"] = title
        movies_dict["genre"] = genre
        movies_dict["rating"] = rating
        return movies_dict
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    else:
        return user_data


##### WAVE 2 #####

def get_watched_avg_rating(user_data):
    ratings_from_user = []
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        for movies in user_data["watched"]:
            ratings_from_user.append(movies["rating"])
        total_sum = sum(ratings_from_user)
        avg_rating = total_sum/(len(ratings_from_user))
        return avg_rating


def get_most_watched_genre(user_data):
    genres_from_user = []
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movies in user_data["watched"]:
            genres_from_user.append(movies["genre"])
        most_popular_genre = max(
            set(genres_from_user), key=genres_from_user.count)
        return most_popular_genre


##### WAVE 3 #####

def get_unique_watched(user_data):
    user_movies = []
    friends_movies = []
    user_unique_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie)
    for watched in user_data["friends"]:
        for movies in watched["watched"]:
            friends_movies.append(movies)
    for users in user_movies:
        if users not in friends_movies:
            user_unique_movies.append(users)
    return user_unique_movies


def remove_dupes(user_data):
    return [i for n, i in enumerate(
        user_data) if i not in user_data[n + 1:]]


def get_friends_unique_watched(user_data):
    friends_watch_movies = []
    user_watch_movies = []
    friends_unique_movies = []
    for movie in user_data["watched"]:
        user_watch_movies.append(movie)
    for watched in user_data["friends"]:
        for movies in watched["watched"]:
            friends_watch_movies.append(movies)
    no_friends_duplicates = remove_dupes(friends_watch_movies)
    # no_friends_duplicates = [i for n, i in enumerate(
    #     friends_watch_movies) if i not in friends_watch_movies[n + 1:]]
    for friends in no_friends_duplicates:
        if friends not in user_watch_movies:
            friends_unique_movies.append(friends)
    return friends_unique_movies


##### WAVE 4 #####

def get_available_recs(user_data):
    #movies_friends_watched = []
    new_recommendations = []
    for friends in user_data["friends"]:
        for watched in friends["watched"]:
            if (watched not in user_data["watched"]) and (watched["host"] in user_data["subscriptions"]):
                new_recommendations.append(watched)
    no_movies_duplicates = remove_dupes(new_recommendations)
    return no_movies_duplicates


##### WAVE 5 #####

def get_new_rec_by_genre(user_data):
    match_genre = get_most_watched_genre(user_data)
    genre_recommendations = []
    for friends in user_data["friends"]:
        for watched in friends["watched"]:
            if (watched not in user_data["watched"]) and (watched["genre"] == match_genre):
                genre_recommendations.append(watched)
    no_genres_duplicates = remove_dupes(genre_recommendations)
    return no_genres_duplicates


def get_rec_from_favorites(user_data):
    recommended_movies = []
    users_favorites = []
    friends_watched = []
    for favorites in user_data["favorites"]:
        users_favorites.append(favorites)
    for friends in user_data["friends"]:
        for watched in friends["watched"]:
            friends_watched.append(watched)
    for movie in users_favorites:
        if movie not in friends_watched:
            recommended_movies.append(movie)
    return recommended_movies
