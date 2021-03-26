def create_movie(title, genre, rating):
    """
    Creates a dictionary representing the description of a movie
    """
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if movie_dict["title"] is None or movie_dict["genre"] is None or\
            movie_dict["rating"] is None:
        return None
    return movie_dict


def add_to_watched(user_data, movie):
    """
    Creates a list of watched movies.
    """
    user_data["watched"] = []
    if movie is not None:
        user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """
    Creates a watchlist/movies to watch in future
    """
    user_data["watchlist"] = []
    if movie is not None:
        user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    """
    user_data = {"watched": [], "watchlist: []}
    type(title) = string

    for each movie in the watchlist
    check if title == to given title:
        if yes: remove that movie from the watchlist AND add that movie to watched
        if not: do nothing
    when done, return the user_data
    """
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


def get_watched_avg_rating(user_data):
    """
    Calculates the average rating of the watched movies.
    """
    len_user_watched = len(user_data["watched"])
    if len_user_watched > 0:
        rating = 0
        for movie in user_data["watched"]:
            rating += movie["rating"]
        return rating / len_user_watched
    else:
        return 0.0


def get_most_watched_genre(user_data):
    """
    Returns the genre from the user list of "watched" movies,
    that is the most frequently watched
    user_data = {"watched": [movie1, movie2, movie3]}
    movie = {"genre": "string"}
    """
    if len(user_data["watched"]) > 0:
        genre_dict = {}  # this dictionary will hold info regarding frequency
        for movie in user_data["watched"]:
            if movie["genre"] in genre_dict.keys():
                genre_dict[movie["genre"]] += 1
            else:
                genre_dict[movie["genre"]] = 1
    else:
        return None

    max_genre_rating = max(genre_dict.values())
    position = list(genre_dict.values()).index(max_genre_rating)
    return list(genre_dict.keys())[position]


def get_friends_watched_titles(user_data):
    """
    Creates the list of titles of movies the user's friends have watched.
    This function is helper. There are no predefined tests for this function.
    """
    friends_watched_titles = []
    for friend in user_data["friends"]:
        for friend_list in friend.values():
            for movie in friend_list:
                friends_watched_titles.append(movie["title"])
    # friends_watched_titles = list(set(friends_watched_titles))
    return list(set(friends_watched_titles))


# def get_user_watched_titles(user_data):
#     """
#     Creates a list of titles of movies the user has watched.
#     This function is helper. There are no tests for this function.
#     """
#     user_watched_titles = []
#     for movie in user_data["watched"]:
#         if movie["title"] not in friends_watched_titles:
#             user_watched_titles.append(movie["title"])
#         # user_watched_titles = list(set(user_watched_titles))
#     return list(set(user_watched_titles))


def get_unique_watched(user_data):
    """
    Creates a list of dictionaries, that represents a list of movies
    that the user has watched, but none of their friends have watched.

    user_data = {
        "watched": [{"title": "Title A"}, {"title": "Title B"}, {"title": "Title C"}],
        "friends": [{"watched": [{"title": "Title A"},{"title": "Title B"}]}, {}, {}]
        }
    friend = {"watched": [movie4, movie5, movie6]}
    movie = {"title": "string"}

    ? Can we assume that movies consideres "same" when the title is the same?
    What if genre differes?

    1. Create a list of movies the friends have watched.
    2. For each movie in the "watched" in user_data check
    if that movie in the list of movies wathced by friends:
    if yes: do nothing
    if no: add this movie dict to the list of objects to return.
    """
    friends_watched_titles = get_friends_watched_titles(user_data)

    user_unique_watched_titles = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_titles:
            user_unique_watched_titles.append(movie["title"])
    user_unique_watched_titles = list(set(user_unique_watched_titles))

    user_unique_watched_list = []
    for title in user_unique_watched_titles:
        user_unique_watched_list.append({"title": title})

    return user_unique_watched_list


def get_friends_unique_watched(user_data):
    """
    Creates a list of dictionaries, that represents a list of movies
    that at least one of the user's friends have watched, but the user has not watched.

    user_data = {
        "watched": [{"title": "Title A"}, {"title": "Title B"}, {"title": "Title C"}],
        "friends": [{"watched": [{"title": "Title A"},{"title": "Title B"}]}, {}, {}]
        }
    """

    user_watched_titles = []
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])
    user_watched_titles = list(set(user_watched_titles))

    friends_watched_titles = get_friends_watched_titles(user_data)

    friends_unique_watched_list = []
    for title in friends_watched_titles:
        if title not in user_watched_titles:
            friends_unique_watched_list.append({"title": title})

    return friends_unique_watched_list

# Wave 4


def get_available_recs(user_data):
    """
    Determines a list of recommended movies:
    user_data = {"subscriptions": ["streaming_service", "streaming_service", "streaming_service"],
                "friends": [{"host":"streaming service"},[},{}]]}

    1. Create a list of users subscriptions.
    2. Select movies from the friends lists which has the same subscriptions.
    3. Check if those movies in the users watched list, if no add to the resulting list.
    """

    user_friends_matched_subscr = []
    for subscr in user_data.get("subscriptions", []):
        # KeyError prevention: dict.get(key, value) will return value in case
        # key not found
        for friend in user_data.get("friends", []):
            for friend_list in friend.values():
                for movie in friend_list:
                    if movie["host"] == subscr:
                        if (movie not in user_data["watched"]) and (
                                movie not in user_friends_matched_subscr):
                            user_friends_matched_subscr.append(movie)
    return user_friends_matched_subscr

    # Wave 5


def get_new_rec_by_genre(user_data):
    """
    Returns a list of recommended movies with users most watched genre.
    Movies in the list have not been watched by user, but have been watched at least by one of his friends.
    """

    # Consider the user's most frequently watched genre.
    user_most_watched_genre = get_most_watched_genre(user_data)

    # Determine a list of recommended movies.
    rec_movies_list = get_friends_unique_watched(user_data)

    resulting_list = [movie
                      for friend in user_data["friends"]
                      for movie in friend["watched"]
                      if movie["genre"] == user_most_watched_genre]

    return resulting_list


def get_rec_from_favorites(user_data):
    """
    Returns a list that includes user's favourite movies that
    none of the user's friends have watched.

    user_data = {"favourites": [a list of movie dictionaries]}
    """

    friends_watched_titles = get_friends_watched_titles(user_data)

    user_fav_titles = []
    for movie in user_data["favorites"]:
        user_fav_titles.append(movie["title"])
    user_fav_titles = list(set(user_fav_titles))

    result_list = []
    for title in [
            movie for movie in user_fav_titles if movie not in friends_watched_titles]:
        result_list.append({"title": title})

    return result_list
