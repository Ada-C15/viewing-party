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
    average_rating = 0.0
    if len(user_data["watched"]) == 0:
        return average_rating

    for movies in user_data.values():
        total_rating = 0.0
        for data in movies:
            total_rating += data["rating"]
        average_rating = total_rating/len(movies)
    return average_rating

def get_most_watched_genre(user_data):
    genre_dict = {}
    for movie in user_data.values():
        for data in movie:
            if data["genre"] not in genre_dict:
                genre_dict[data["genre"]] = 1
            else:
                genre_dict[data["genre"]] += 1
    for key, value in genre_dict.items():
        if value == max(genre_dict.values()):
            return key


# test_wave_03
def get_unique_watched(user_data):
    not_watched_list = []
    track_list = []

    for movie in user_data["watched"]:
        track_list.append(movie["title"])

    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j]["title"] in track_list:
                track_list.pop(user_data["friends"][i]["watched"].index(user_data["friends"][i]["watched"][j]))

    for movie in track_list:
        not_watched_list.append({"title" : movie})

    return not_watched_list

def get_friends_unique_watched(user_data):
    not_watched_list = []
    track_list = []

    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j]["title"] not in track_list:
                track_list.append(user_data["friends"][i]["watched"][j]["title"])

    for i in range(len(user_data["watched"])):
        title_name = user_data["watched"][i]["title"]
        if title_name in track_list:
            track_list.pop(track_list.index(title_name))

    for movie in track_list:
        not_watched_list.append({"title" : movie})

    return not_watched_list


# test_wave_04
def get_available_recs(user_data):
    recommended_movies = []

    for movies in user_data["friends"]:
        for i in range(len(movies["watched"])):
            if movies["watched"][i]["host"] in user_data["subscriptions"]:
                if movies["watched"][i] not in recommended_movies:
                    recommended_movies.append(movies["watched"][i])

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

    for data in user_data["friends"]:
        for i in range(len(data["watched"])):
            if data["watched"][i]["genre"] == fav_genre and data["watched"][i]["title"] not in movies_list:
                recommended_movies.append(data["watched"][i])

    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []

    not_watched_listed = []
    friends_list = []
    for data in user_data["friends"]:
        for i in range(len(data["watched"])):
            friends_list.append(data["watched"][i])

    for i in range(len(user_data["watched"])):
        if user_data["watched"][i] not in friends_list and user_data["watched"][i] in user_data["favorites"]:
            recommended_movies.append(user_data["watched"][i])

    return recommended_movies
