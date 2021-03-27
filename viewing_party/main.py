def create_movie(title, genre, rating):
    """Create and return dictionary holding movie details."""
    movies_dict = {}
    if title and genre and rating:
        movies_dict["title"] = title
        movies_dict["genre"] = genre
        movies_dict["rating"] = rating
        return movies_dict
    elif not title or not genre or not rating:
        return None

def add_to_watched(user_data, movie):
    """Add a movie to user's 'WATCHED' list."""
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """Add a movie to a user's 'WATCHLIST'."""
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """Remove watched movies from the user's 'WATCHLIST' 
        and add them to the 'WATCHED' list. 
        """
    for movie_in_list in user_data["watchlist"]:
    # my_index allows us to access elements in the list we are working with
        my_index = len(user_data["watchlist"]) 
        if title in user_data["watchlist"][my_index-1]["title"]:
            movie_data = user_data["watchlist"][my_index-1]
            user_data["watchlist"].remove(movie_data)
            user_data["watched"].append(movie_data)
            return user_data
        elif title not in user_data["watchlist"][my_index-1]["title"]:
            return user_data

def get_watched_avg_rating(user_data):
    """Calculate average rating of movies in user's 'WATCHED' list."""
    hold_ratings = []
    for movie_in_watched in user_data["watched"]:
        rating = movie_in_watched["rating"]
        hold_ratings.append(rating)
    try: 
        divisor = len(user_data["watched"])
        avg_rating = sum(hold_ratings) / (divisor)
    except ZeroDivisionError as err:
        return 0.0
    return avg_rating 

def get_most_watched_genre(user_data):
    """Determine and return the genre the user watches most frequently."""
    hold_genres = {}
    if user_data["watched"] == []:
            return None        
    for movies_in_watched in user_data["watched"]:
        genre = movies_in_watched["genre"] 
        if genre not in hold_genres:
            hold_genres[genre] = 1
        else:
            hold_genres[genre] += 1
    most_frequent = max(hold_genres)
    return most_frequent 

def get_unique_watched(user_data):
    """Determine and return a list of movies that the user has watched
        but that the user's friends have not watched.
        """
    movies_user_watched = []
    movies_friends_watched = []
    unique_titles = []
    for movie_info in user_data["watched"]: 
        movies_user_watched.append(movie_info) 
    for friend in user_data["friends"]:
        for friend_movie_info in friend["watched"]:
            movies_friends_watched.append(friend_movie_info)
    for entry in movies_user_watched:
        if entry not in movies_friends_watched:
            unique_titles.append(entry)
    return unique_titles

def get_friends_unique_watched(user_data):
    """Determine and return a list of movies that the user's friends
        have watched but that the user has not watched.
        """
    user_watched = []
    friends_watched = []
    return_watched = []
    for film in user_data["watched"]:
        user_watched.append(film)
    for friend in user_data["friends"]:
        for friend_data in friend["watched"]:
            friends_watched.append(friend_data)
    # list comprehension to address duplicate dicts       
    dry_friends_watched = [i for n, i in enumerate(friends_watched) if i not in friends_watched[n + 1:]]
    for relevant_movie in dry_friends_watched:
        if relevant_movie not in user_watched:
            return_watched.append(relevant_movie)
    return return_watched

def get_available_recs(user_data):
    """Determine and return a list of movies that the user has not watched,
        that at least one of the user's friends has watched and that is
        available to the user given their subscriptions.
        """
    recommended_movies = []
    for friend_watch_list in user_data["friends"]: 
        for movie_host_detail in friend_watch_list["watched"]:
            if (movie_host_detail not in user_data["watched"]) and (movie_host_detail["host"] in user_data["subscriptions"]):
                recommended_movies.append(movie_host_detail)
    # address duplicates with list comprehension
    dry_recommended = [i for n, i in enumerate(recommended_movies) if i not in recommended_movies[n + 1:]]
    return dry_recommended

def get_new_rec_by_genre(user_data):
    """Determine and return a list of movie recommendations that the user
        has not watched, that at least one of the user's friends has watched,
        and whose genre matches the user's favorite genre.
        """
    genre_for_compare = get_most_watched_genre(user_data)
    recs_by_genre = []
    for friend_watched_list in user_data["friends"]:
        for friend_movie in friend_watched_list["watched"]: 
            if (friend_movie not in user_data["watched"]) and (friend_movie["genre"] == genre_for_compare):
                recs_by_genre.append(friend_movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    """Determine and return a list of movie recommendations that none of the
        user's friends have seen and that is in the user's 'FAVORITES' list.
        """
    hold_friend_watched = []
    hold_my_watched = []
    for friend_watched_list in user_data["friends"]:
        for friend_movie_watched in friend_watched_list["watched"]: 
            hold_friend_watched.append(friend_movie_watched)
    for my_movie in user_data["watched"]:
        if my_movie in user_data["favorites"]:
            hold_my_watched.append(my_movie) 
    for their_movies in hold_friend_watched:
        if their_movies in hold_my_watched:
            hold_my_watched.remove(their_movies)
    return hold_my_watched
