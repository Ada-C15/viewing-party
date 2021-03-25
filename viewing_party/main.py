# test_wave_01
def create_movie(movie_title, genre, rating):
    movie_dict = {}
    if not movie_title or not genre or not rating:
        return None
    else:
        movie_dict["title"] = movie_title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            track = user_data["watchlist"].pop()
            user_data["watched"].append(track)
    return user_data


# test_wave_02
def get_watched_avg_rating(user_data):
    total_rating = 0.0
    if len(user_data["watched"]) == 0:
        return total_rating

    for movies in user_data["watched"]:
        total_rating += movies["rating"]

    return total_rating/len(user_data["watched"])


def get_most_watched_genre(user_data):
    genre_dict = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 1
        else:
            genre_dict[movie["genre"]] += 1
            
    for key, value in genre_dict.items():
        if value == max(genre_dict.values()):
            return key


# test_wave_03
def get_unique_watched(user_data):
    movies_list = [movie for movie in user_data["watched"]]

    for friend in user_data["friends"]:
        for movies_watched in friend["watched"]:
            if movies_watched in movies_list:
                movies_list.pop(friend["watched"].index(movies_watched))

    return movies_list


def get_friends_unique_watched(user_data):
    movies_list = []

    for friend in user_data["friends"]:
        for movies_watched in friend["watched"]:
            if movies_watched not in movies_list:
                movies_list.append(movies_watched)
    
    for movies_watched in user_data["watched"]:
        if movies_watched in movies_list:
            movies_list.pop(movies_list.index(movies_watched))

    return movies_list


# test_wave_04
def get_available_recs(user_data):
    recommended_movies = []

    for friend in user_data["friends"]:
        for movies_watched in friend["watched"]:
            if movies_watched["host"] in user_data["subscriptions"] and \
                    movies_watched not in recommended_movies:
                recommended_movies.append(movies_watched)

    return recommended_movies


# test_wave_05
def get_new_rec_by_genre(user_data):
    recommended_movies = []

    genre_list = []
    movies_list = []
    for movies in user_data["watched"]:
        genre_list.append(movies["genre"])
        movies_list.append(movies["title"])

    try:
        fav_genre = max(genre_list)
    except ValueError:
        return recommended_movies

    for friend in user_data["friends"]:
        for watched_movie in friend["watched"]:
            if watched_movie["genre"] == fav_genre and \
                    watched_movie["title"] not in movies_list:
                recommended_movies.append(watched_movie)

    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []

    friends_list = []
    for friend in user_data["friends"]:
        for watched_movie in friend["watched"]:
            friends_list.append(watched_movie)

    for watched_movie in user_data["watched"]:
        if watched_movie not in friends_list and \
                watched_movie in user_data["favorites"]:
            recommended_movies.append(watched_movie)

    return recommended_movies
