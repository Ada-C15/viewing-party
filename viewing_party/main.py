# WAVE One
def create_movie(movie_title, genre, rating):
    movie = {}
    movie['title'] = movie_title
    movie['genre'] = genre
    movie['rating'] = rating

    for values in movie.values():
        if values == None:
            return None

    return movie


def add_to_watched(user_data, movie):
    new_entry = user_data["watched"]
    new_entry.append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    new_entry = user_data["watchlist"]
    new_entry.append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
            return user_data
    else:
        return user_data


# Wave Two

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
    most_watched = {}
    popular_genre = None
    for movie in user_data["watched"]:
        if movie["genre"] not in most_watched:
            most_watched[movie["genre"]] = 1
        else:
            most_watched[movie["genre"]] += 1
        popular_genre = max(most_watched, key=most_watched.get)

    return popular_genre

# WAVE THREE (version4)

def get_unique_watched(user_data):
    unique_watched = []
    friends_movies = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friends_movies:
                friends_movies.append(movie)

    for movie in user_data["watched"]:
        if movie not in friends_movies:
            unique_watched.append(movie)

    return (unique_watched)


def get_friends_unique_watched(user_data):
    friend_unique_watched = []
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_unique_movies:
                friends_unique_movies.append(movie)

    for movie in friends_unique_movies:
        if movie not in user_data["watched"]:
            friend_unique_watched.append(movie)

    return (friend_unique_watched)


# Wave Four


def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies


# Wave Five (version3)

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


