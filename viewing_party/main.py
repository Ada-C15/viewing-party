# WAVE 1

def create_movie(title, genre, rating):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    for value in movie.values():
        if value is None:
            return None
    return movie    

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


# WAVE 2

def get_watched_avg_rating(user_data):
    # determine the average rating of all watched movies
    if user_data["watched"] == []:
        return 0.0
    else:
        sum = 0
        for movie in user_data["watched"]:
            sum += movie["rating"]
        avg = sum/len(user_data["watched"])
        return avg

def get_most_watched_genre(user_data):
    if user_data["watched"] == []:
        return None
    else:
        user_movie_genres = []
        for movie in user_data["watched"]:
            user_movie_genres.append(movie["genre"])

    # determine the most watched genre
    genre_frequency = {}
    for genre in user_movie_genres:
        if genre not in genre_frequency:
            genre_frequency[genre] = 1
        else:
            genre_frequency[genre] += 1

    for genre, value in genre_frequency.items():
        if value == max(genre_frequency.values()):
            return genre


# WAVE 3

def get_unique_watched(user_data):
    if user_data["watched"] == []:
        return []

    friends_list = []
    for friend in user_data["friends"]:
        for value in friend.values():
            i = 0
            while i < len(value):
                friends_list.append(value[i])
                print(f"For index {i} the value is {value[i]}")
                i += 1

    # compare lists and return movies only user has watched
    unique_watched = []
    for title in user_data["watched"]:
        if title not in friends_list:
            unique_watched.append(title)
    return unique_watched

def get_friends_unique_watched(user_data):
    # compare lists and return movies only friends have watched
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for title in friend["watched"]:
            if title not in user_data["watched"] \
                and title not in friends_unique_watched:
                friends_unique_watched.append(title)
    return friends_unique_watched


# WAVE 4

def get_available_recs(user_data):
    # determine list of recommended movies by user's subscriptions
    available_recs = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"] \
                and movie["host"] not in user_data["watched"] \
                    and movie not in available_recs:
                available_recs.append(movie)
    return available_recs


# WAVE 5

def get_new_rec_by_genre(user_data):
    # populate user's movie title list and movie genre list
    user_movie_list = []
    user_movie_genres = []
    for movie in user_data["watched"]:
        user_movie_list.append(movie["title"])
        user_movie_genres.append(movie["genre"])
    
    # determine user's favorite genre
    user_fave_genre = get_most_watched_genre(user_data)
    if user_fave_genre == None:
        return []

    # determine list of recommended movies by user's favorite genre
    new_rec_by_genre = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == user_fave_genre \
                and movie["title"] not in user_movie_list \
                    and movie not in new_rec_by_genre:
                new_rec_by_genre.append(movie)
    return new_rec_by_genre 

def get_rec_from_favorites(user_data):
    # determine list of recommended movies by user's favorite titles
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    rec_from_favorites = []
    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            rec_from_favorites.append(movie)
    return rec_from_favorites
