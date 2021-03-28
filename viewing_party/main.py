# test_wave_01

def create_movie(movie_title=str, genre=str, rating=float):
    """Creates a ``new_movie`` that will be added to the user's list.

    Args:
        movie_title (str): The title of a movie. Defaults to str.
        genre (str): The movie genre. Defaults to str.
        rating (float): The movie rating. Defaults to float.

    Returns:
        new_movie: A dictionary containing the keys and values
            for a movie. Returns None for invalid arguments.
    """

    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }

    if not movie_title or not genre or not rating:
        return None
    else:
        return new_movie

def add_to_watched(user_data, movie):
    """Adds a ``movie`` to the user's ``watched`` movies list.

    Args:
        user_data (dict): Represents the user's ``watched`` list.
        movie (dict): Represents a movie with a ``title``, ``genre``,
            and ``rating``.

    Returns:
        user_data (dict): The user's data, with their ``watched``
            movies list updated.
    """

    user_movies = user_data["watched"]
    if movie not in user_movies:
        user_movies.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """Adds the ``movie`` to the user's ``watchlist``.

    Args:
        user_data (dict): Represents the user's ``watchlist``.
        movie (dict): Represents a movie with a ``title``, ``genre``,
            and ``rating``.

    Returns:
        user_data (dict): The user's data, with their ``watchlist``
            updated.
    """

    watchlist = user_data["watchlist"]
    if movie not in watchlist:
        watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    """Allows the user to update their movies lists based
    on a ``title`` they have watched.

    Args:
        user_data (dict): Represents the user's data, with their
            lists of movies.
        title (str): Represents the ``title`` of the movie
            the user has watched.

    Returns:
        user_data (dict): The user's data, with their lists 
            of movies updated.
    """

    watchlist = user_data["watchlist"]
    for entry in watchlist:
        if entry["title"] == title:
            watchlist.remove(entry)
            add_to_watched(user_data, entry)
    return user_data

# test_wave_02

def get_watched_avg_rating(user_data):
    """Calculates the average rating of all movies in the user's ``watched`` movies list.

    Args:
        user_data (dict): Represents the user's data, with their
            list of ``watched`` movies, rated.

    Returns:
        float: The average rating of all movies in the user's
            ``watched`` movies list. Unrated movies default to 0.0.
    """

    user_movies = user_data["watched"]
    movies_list_length = len(user_movies)
    default_rating = 0.0
    avg_rating = 0.0

    if movies_list_length > 0:
        for movie in user_movies:
            avg_rating += movie["rating"]
    else:
        return default_rating
    return avg_rating / float(movies_list_length)

def get_most_watched_genre(user_data):
    """Determines which genre is most frequent in the user's
    ``watched`` list.

    Args:
        user_data (dict): Represents the user's data, with their
            ``watched`` list of movies.

    Returns:
        popular_genre (str): The movie genre that is the most
            frequently watched.
    """

    user_movies = user_data["watched"]
    all_genres = {}
    popular_genre = None
    pop_val = 0

    for movie in user_movies:
        genre = movie["genre"]
        if genre not in all_genres:
            all_genres[genre] = 1
        else:
            all_genres[genre] = all_genres[genre] + 1

    for gen in all_genres:
        if all_genres[gen] > pop_val:
            pop_val = all_genres[gen]
            popular_genre = gen
    return popular_genre

# test_wave_03

def get_unique_watched(user_data):
    """Determines which movies the user has watched, but none of their friends
    have watched.

    Args:
        user_data (dict): Represents the user's data, with their
            ``watched`` list of movies and ``friends`` list.

    Returns:
        user_unique_movies (list): a list of dictionaries, that 
            represents a list of movies.
    """

    user_movies = user_data["watched"]
    all_friends = user_data["friends"]
    friends_movie_list = []
    user_unique_movies = user_movies

    for friends in all_friends:
        for entry in friends["watched"]:
            friends_movie_list.append(entry)

    for movie in friends_movie_list:
        if movie in user_unique_movies:
            user_unique_movies.remove(movie)
    return user_unique_movies

def get_friends_unique_watched(user_data):
    """Determines which movies at least one of the user's friends have watched, but the user has not watched.

    Args:
        user_data (dict): Represents the user's data, with their
            ``watched`` list of movies and ``friends`` list.

    Returns:
        user_must_see (list): A list of dictionaries, that 
        represents a list of movies.
    """

    user_movies = user_data["watched"]
    all_friends = user_data["friends"]
    friends_movie_list = []
    user_must_see = []

    for friends in all_friends:
        for entry in friends["watched"]:
            if entry not in friends_movie_list:
                friends_movie_list.append(entry)

    for movie in friends_movie_list:
        if movie not in user_movies:
            user_must_see.append(movie)
    return user_must_see

# test_wave_04

def get_available_recs(user_data):
    """Determines a list of movie recommendations based in movies that the user didn't watch and their ``subscriptions`` in streaming services.

    Args:
        user_data (dict): Represents the user's data, with their
            ``watched`` list of movies, a ``friends`` list, and 
            their ``subscriptions``.

    Returns:
        recommendations (list): A list of movies recommended by 
            friends.
    """

    user_subscriptions = user_data["subscriptions"]
    user_watched = user_data["watched"]
    all_friends = user_data["friends"]
    recommendations = []

    if not user_watched:
        for friend in all_friends:
            for rec in friend["watched"]:
                if rec["host"] in user_subscriptions and rec not in recommendations:
                    recommendations.append(rec)
    return recommendations

# test_wave_05

def get_new_rec_by_genre(user_data):
    """Determines a list of recommended movies considering the user's most frequently watched movie ``genre``.

    Args:
        user_data (dict): Represents the user's data, with their
            list of movies, favorite movie genre, and a ``friends``
            list.

    Returns:
        new_recs (list): A list of recommended movies based in
            the user's favorite genre.
    """

    user_watched = user_data["watched"]
    all_friends = user_data["friends"]
    fav_genre = get_most_watched_genre(user_data)
    new_recs = []

    for friend in all_friends:
        for movie in friend["watched"]:
            if movie["title"] not in new_recs and movie["genre"] == fav_genre:
                new_recs.append(movie)

    for title in new_recs:
        if title in user_watched:
            new_recs.remove(title)
    return new_recs

def get_rec_from_favorites(user_data):
    """Determines a list of recommended movies considering the user's favorite movies.

    Args:
        user_data (dict): Represents the user's data, with their
            list of movies, favorite movies, and a ``friends``
            list.

    Returns:
        recommendations (list): A list of recommended movies based
            in the user's favorite movies.
    """

    user_favs = user_data["favorites"]
    all_friends = user_data["friends"]
    recommendations = []

    for movie in user_favs:
        recommendations.append(movie)

    for friend in all_friends:
        friend_movie_list = friend["watched"]
        for movie in friend_movie_list:
            if movie in recommendations:
                recommendations.remove(movie)
    return recommendations

