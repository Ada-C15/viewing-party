def create_movie(title, genre, rating):
    """Builds movie record"""
    if title and genre and rating:
        return {
        "title": title,
        "genre": genre,
        "rating": rating
        }
    else:
        return None

def add_to_watched(user_data, movie):
    """Adds watched movie to the watched list"""
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """Adds movie to the watchlist"""
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """Checks if movie been watched"""
    for i in range(len(user_data["watchlist"])):
        movie = user_data["watchlist"][i]
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    """Calculates the average rating of the watched movies"""
    if user_data["watched"]:
        rating_sum = 0
        for movie in  user_data["watched"]:
            rating_sum += movie["rating"]
        return rating_sum/len(user_data["watched"])
    else:
        return 0.0

def get_most_watched_genre(user_data):
    """Determines the most popular genre"""
    # Count the number of views for each genre
    if user_data["watched"]:
        most_popular_genre = {}
        for movie in user_data["watched"]:
            for key, genre in movie.items():
                if genre not in most_popular_genre:
                    most_popular_genre[genre]=0
                else:
                    most_popular_genre[genre]+=1
        # Keep only the most popular genre
        most_popular_genre = max(most_popular_genre,key=most_popular_genre.get)
        return most_popular_genre
    else:
        return None

def get_unique_watched(user_data):
    """Determines movies the user has watched, but their friends haven't"""
    # TODO: learn list comprehension and end this nonsense
    user_movies = set()
    for movie in user_data["watched"]:
        user_movies.add(movie["title"])
    friends_movies = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])
    result = user_movies - friends_movies
    unique_movies = []
    for movie in result: 
        unique_movies.append({"title": movie})
    return unique_movies

    # First approach:
    # user_watched = user_data["watched"]
    # friends_watched = []
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         friends_watched.append(movie)
    # result = []
    # for user_movie in user_watched:
    #     unique_movie = True
    #     for friend_movie in friends_watched:
    #         if friend_movie["title"] == user_movie["title"]:
    #             unique_movie = False
    #     if unique_movie:
    #         result.append(user_movie)
    # return result

def get_friends_unique_watched(user_data):
    """Determines movies user's friends have watched, but the user has not"""
    user_movies = set()
    [user_movies.add(movie["title"]) for movie in user_data["watched"]]

    friends_movies = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])
    result = friends_movies - user_movies

    return [{"title": movie} for movie in result]

def get_available_recs(user_data):
    """Determines a list of recommended movies that are available for the user in their subscriptions"""
    friend_recs = get_friends_unique_watched(user_data)
    rec_titles = []
    [rec_titles.append(movie["title"]) for movie in friend_recs]

    rec_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie["title"] in rec_titles) and (movie["host"] in user_data["subscriptions"]):
                rec_movies.append({"title": movie["title"], "host": movie["host"]})

    return [dict(t) for t in {tuple(d.items()) for d in rec_movies}]

def get_new_rec_by_genre(user_data):
    """
    Returns list of recommended movies, that:
    - The user has not watched;
    - User's friends have watched;
    - User's fav genre.
    """
    friends_recs = get_friends_unique_watched(user_data)
    genre = get_most_watched_genre(user_data)
    rec_titles = []
    [rec_titles.append(movie["title"]) for movie in friends_recs]
    rec_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie["title"] in rec_titles) and (movie["genre"] == genre):
                rec_movies.append({"title": movie["title"], "genre": movie["genre"]})

    return [dict(t) for t in {tuple(d.items()) for d in rec_movies}]

def get_rec_from_favorites(user_data):
    """Gets the user's favorite movies, their friends haven't seen"""
    user_movies = get_unique_watched(user_data)
    rec_titles = []

    for movie in user_movies:
        if movie in user_data["favorites"]:
            rec_titles.append(movie)

    return rec_titles