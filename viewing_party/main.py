# FUNCTION  FOR TESTS 1, 2, 3,  4  WAVE 1 PASSED
def create_movie(movie_title, genre, rating):
    '''
    Creates a dictionary new-movie with the inputs as values.
    Input: three parameters two strings, one number.
    Output : returns the dictionary new-movie.
    '''

    new_movie = {"title": movie_title,
                "genre": genre,
                "rating": rating}
    for key, value in new_movie.items():
        if value == None or value == "" or value == False:
            new_movie = None
    return new_movie

# FUNCTION FOR TEST 5 WAVE 1 PASSED
def add_to_watched(user_data, movie):
    '''
    Adds movie (dictionary) to the "watched" list.
    Input: two parameters user_data(dictionary of nested data structures) 
    and movie (a list of dictionaries).
    Output: returns updated user_data with movie in updated watched list.
    '''

    user_data["watched"].append(movie)
    return user_data

# FUNCTION  FOR TEST 6 WAVE 1 PASSED
def add_to_watchlist(user_data, movie):
    '''
    Adds movie (dictionary) to the watchlist list.
    Input: two parameters user_data (dictionary of nested data structures) 
    and movie (a list of dictionaries).
    Output: returns updated user_data with movie in updated watchlist list.
    '''

    user_data["watchlist"].append(movie)
    return user_data

# FUNCTION FOR TEST 7, 8, 9 WAVE 1 PASSED
def watch_movie(user_data, movie_title):
    ''' 
    Moves movie from watchlist list to empty watched list.
    Input: two parameters user_data (dictionary of nested data structures) 
    and a movie_title (string).
    Output: returns updated dictionary user_data with movie moved from 
    user_data watchlist list to user_data watched list.
    '''
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# FUNCTION FOR TESTS 10, 11 WAVE 2  PASSED
def get_watched_avg_rating(user_data):
    '''
    Calculate the average rating of all movies in the watched list.
    Input: one parameter user_data (dictionary of nested data structures).
    Output: returns return the average rating (float).
    '''

    sum = 0
    if len(user_data["watched"]) == 0:
        return 0
    else:
        for movie in user_data["watched"]:
            sum += movie["rating"]
        average = sum / (len(user_data["watched"]))
        return average

# FUNCTION FOR TESTS 12, 13 WAVE 2  PASSED!!
def get_most_watched_genre(user_data):
    '''
    Determines most watched genre from watched list movies.
    Input: nested dictionary of lists
    Output: returns genre that is the most frequently watched
    '''

    if len(user_data["watched"]) == 0:
        return None
    else:
        genres_count = {}
        for movie in user_data["watched"]:
            if not movie["genre"] in genres_count.keys():
                genres_count[movie["genre"]] = 1
            elif movie["genre"] in genres_count.keys():
                genres_count[movie["genre"]] += 1

        # Find most watched in dictionary by adding the fist value to a 
        # variable
        most_watched_genre = list(genres_count.keys())[0]
        for key, value in genres_count.items():
            # compare that next item's value in the dictionary with value 
            # of most watched genere so far stored
            # if greater than, then replace value in variable
            if genres_count[most_watched_genre] < value:
                most_watched_genre = key
        return most_watched_genre


# FUNCTION FOR TESTS 14, 15 WAVE 3  PASSED
def get_unique_watched(user_data):
    '''
    Creates list of unique movies (dictionaries), from user watched list
    not in friends watched list.
    Input : one parameter user data (a dictionary of lists)
    Output: return a list of dictionaries that represents list of movies
    '''

    friends_movies = user_data['friends']
    all_friends_movies = []
    for friend_d in friends_movies:
        all_friends_movies += friend_d['watched']

    # list comprehension that gets only the titles(values) so I can turn 
    # into set
    friends_l = [titles['title'] for titles in all_friends_movies]
    friends_s = set(friends_l)

    user_movies = user_data['watched']
    user_unique_movies = [title for title in user_movies \
        if title['title'] not in friends_s]
    return user_unique_movies

# FUNCTION FOR TESTS 15, 16, 17, 18 WAVE 3  PASSED
def get_friends_unique_watched(user_data):
    '''
    Creates a list of unique movies(dictionaries) from friends watched list
    not in user's watched list.
    Input : one parameter user data (a dictionary of lists).
    Output: a list of of movies.
    '''

    # Movies at least one the friends have watched, but user has not watched.
    friends_movies = user_data['friends']
    all_friends_movies = []

    for friend_d in friends_movies:
        all_friends_movies += friend_d['watched']

    user_movies = user_data['watched']
    friends_uniq_movies = []

    for movie in all_friends_movies:
        if movie not in user_movies and movie not in friends_uniq_movies:
            friends_uniq_movies.append(movie)

    return friends_uniq_movies

# FUNCTION FOR TESTS 19, 20 - WAVE 4 PASSED
def get_available_recs(user_data):
    '''
    Creates list of recommended movies from friends not in users watched 
    list with user's suscription service options.
    Input:  one parameter: user_data (dictionary of nested data structures).
    Output: return a list of movie recomendations  
    '''
    
    friends_uniq_movies = get_friends_unique_watched(user_data)

    # create list of recommended movies (list of dictionary of movies 
    # with titles, genre, host, etc) empty first
    recommendations = []
    # iterate over get_friends_unique to pull host value
    for movie in friends_uniq_movies:  
        # If value in list of subscriptions (user_data["subscriptions"])
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations

# FUNCTION FOR TESTS 21, 22, 23, 24 WAVE 5 - PASSED
def get_new_rec_by_genre(user_data):
    '''
    Creates a list of movies (dictionaries) from friends watch list not 
    in user's watched list by most watched genre.
    Input: one parameter - user_data (list of dictionaries).
    Output: returns list of friends recommended movies by genre
    '''

    # get_friends_unique_watched(user_data) (all friends) list
    friends_uniq_movies = get_friends_unique_watched(user_data)  

    # all get_most_watched_genre(user_data) - string
    most_watched_genre = get_most_watched_genre(user_data)

    # create list of recommended_by_genre []
    recommended_by_genre = []
    # to look at genre values which is a string compare if 
    # most_watched_genre is same movie['genre']
    for movie in friends_uniq_movies:  
        if most_watched_genre == movie["genre"]:
            recommended_by_genre.append(movie)

    return recommended_by_genre

# FUNCTION FOR TEST 25 WAVE 5 - PASSED
def get_rec_from_favorites(user_data):
    '''
    Creates list of recommended movies from user's favorites that haven't
    been watched by any user's friends.
    Input: one parameter - user_data (list of dictionaries).
    Return the list of recommended user favorite movies.
    '''

    # user's favorite movies list of movie dictionaries 
    favorite_movies = user_data["favorites"]

    # find friends watched (list of all friends movies)
    friends_watched_l = []
    for friend_movie in user_data["friends"]:
        friends_watched_l += friend_movie["watched"]

    # iterate and append  movies not in friends movies  (no friends have
    #  watched it)
    rec_from_favorites = []
    i = 0
    for movie in favorite_movies:   
        if not movie in friends_watched_l:
            rec_from_favorites.append(movie)
            
    return rec_from_favorites
