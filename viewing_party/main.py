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

    if movie not in user_data["watched"]:
        user_data["watched"].append(movie)
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

    if movie not in user_data["watchlist"]:
        user_data["watchlist"].append(movie)
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

    for entry in user_data["watchlist"]:
        if entry["title"] == title:
            user_data["watchlist"].remove(entry)
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

    if movies_list_length == 0:
        return None
        
   for movie in user_movies:
        avg_rating += movie["rating"]
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

    all_genres = {}
    popular_genre = None
    pop_val = 0

    for movie in user_data["watched"]:
        genre = movie["genre"]  # for better readability
        if genre not in all_genres:
            all_genres[genre] = 1
        else:
            all_genres[genre] += 1  # update the value

    for gen in all_genres:
        if all_genres[gen] > pop_val:
            pop_val = all_genres[gen]
            popular_genre = gen
    return popular_genre

# test_wave_03

# NEW: Helper function: gets the movies all friends watched.

def get_friends_movies(user_data):
    """A helper function to get a list of movies the user's friends have watched.

    Args:
        user_data (dict): Represents the user's data, with their ``friends`` list.

    Returns:
        friends_movies (list): A list of dictionaries, representing movies the user's friends have watched. 
    """

    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movies:
                friends_movies.append(movie)
    return friends_movies

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

    friends_movies = get_friends_movies(user_data)
    user_unique_movies = []

    for movie in user_data["watched"]:
        if movie not in user_unique_movies and movie not in friends_movies:
            user_unique_movies.append(movie)
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

    friends_movies = get_friends_movies(user_data)
    user_must_see = []

    for movie in friends_movies:
        if movie not in user_data["watched"] and movie not in user_must_see:
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

    subscriptions = user_data["subscriptions"]
    friends_movies = get_friends_movies(user_data)
    recommendations = []

    for movie in friends_movies:
        if movie["host"] in subscriptions and movie not in recommendations:
            recommendations.append(movie)
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

    friends_movies = get_friends_movies(user_data)
    fav_genre = get_most_watched_genre(user_data)
    new_recs = []

    for movie in friends_movies:
            if movie not in new_recs and movie["genre"] == fav_genre:
                new_recs.append(movie)
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

    friends_movies = get_friends_movies(user_data)
    recommendations = []

    for movie in user_data["favorites"]:
        recommendations.append(movie)

    for movie in friends_movies:
        if movie in recommendations:
            recommendations.remove(movie)
    return recommendations
