def create_movie(movie_title, genre, rating):

    # Create a new movie
    new_movie = {"title": movie_title, "genre": genre, "rating": rating}

    if new_movie["title"] == None or new_movie["genre"] == None or new_movie["rating"] == None:
        return None
    return new_movie

def add_to_watched(user_data, movie):

    # Add movie in the list of movies that the user has already watched
    user_data = {
        "watched": [movie]
    }
    return user_data

def add_to_watchlist(user_data, movie):

    # Add movie in the user's watchlist
    user_data = {
        "watchlist": [movie]
    }
    return user_data

def watch_movie(user_data, title):

    # Check if title is in a movie in the user's watchlist 
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
        # Add movie in the list of watched movie and remove it from the watchlist
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data

def get_watched_avg_rating(user_data):

    # Setup
    movie_rating = []
    avg_rating = None

    # Check if there are movies in the list of watch movies
    if len(user_data["watched"]) == 0:
        avg_rating = 0.0
        return avg_rating 
    # Check if there are any movie in the list of watch movies
    else:
        for movie in user_data["watched"]:
        # Add movie in a new list
            movie_rating.append(movie["rating"])
        # Calculate the average rating
        avg_rating = sum(movie_rating)/len(movie_rating)
        return avg_rating

def get_most_watched_genre(user_data):

    # Setup
    l_genre =  {}
    
    # Check if movie genre is in the l_genre dictionary and if not, we add the genre as a key with a value of 1 
    # Otherwise, increment the value by 1
    for movie in user_data["watched"]:
        if movie["genre"] not in l_genre:
            l_genre[movie["genre"]] = 1
        else:
            l_genre[movie["genre"]] += 1
    # Setup
    number= 0
    popular_genre= None

    # Find genre with the highest value in the l_genre dictionary
    for key in l_genre:
    # Compare genre value with number and update number if genre value is highest than number
        if l_genre[key] > number:
            number = l_genre[key]
            popular_genre = key
    return popular_genre

def get_unique_watched(user_data):
    
    #Setup
    movies_watched = []
    unique_movies = []
    user_friends = user_data["friends"]

    # Add movies that friends have watched in the movies_watched list
    for friend in user_friends:
        for value in friend.values():
            movies_watched.extend(value)

    # Check if movie that user has wacthed is in the movies_watched list
    for movie in user_data["watched"]:
        if movie in movies_watched:
            continue
        unique_movies.append(movie)
    print(movies_watched)
    return unique_movies

def get_friends_unique_watched(user_data):

    #Setup
    movies_watched = []
    unique_movies = []
    user_friends = user_data["friends"]

    # Add movies that friends have watched in the movies_watched list
    for friend in user_friends:
        for value in friend.values():
            movies_watched.extend(value)

    # Check if movie not in the unique_movies list and not in the user watched list    
    for movie in movies_watched:
        if movie not in unique_movies:
            if movie in user_data["watched"]:
                continue
            unique_movies.append(movie)
    return unique_movies

def get_available_recs(user_data):

    # Setup
    recommended_movies = []
    unique_watched = get_friends_unique_watched(user_data)

    # Check if the host of the movie that only friends have watched is in the user's subcription
    for movie in unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies


def get_new_rec_by_genre(user_data):

    # Setup
    recd_movies = get_friends_unique_watched(user_data)
    unique_genre = get_most_watched_genre(user_data)
    recd_genre = []

    # Check if genre's movie that only friends have watched is the same as user's most frequent genre.
    for movie in recd_movies:
        if movie["genre"] == unique_genre:
            recd_genre.append(movie)
    return recd_genre 

def get_rec_from_favorites(user_data):
    
    # Setup
    rec_fav = []
    user_unique_watched = get_unique_watched(user_data)

    #Check if movies that only the user has watched are in user's favorites list of movies
    for movie in user_unique_watched:
        if movie in user_data["favorites"]:
            rec_fav.append(movie)
    return rec_fav





