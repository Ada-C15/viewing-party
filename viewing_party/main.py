
def create_movie(title, genre, rating):
    """
    inputs: title (str), genre (str), rating (num)
    outputs: a dictionary with 3 key-value pairs, which each correspond to one of the parameters
    """

    # initialize a dictionary
    movie_dict = {}

    # if ALL parameter values are truthy, add keys and values to dictionary and return dictionary
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

    # if ANY of the parameters return falsy, the function should return None
    return None

def add_to_watched(user_data, movie):
    """
    inputs: user_data (a dictionary with an empty list as its value) and movie (dictionary)
    outputs: returns the updated user_data dictionary
    """

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    """
    inputs: user_data (a dictionary with an empty list as its value) and movie (dictionary)
    outputs: returns the updated user_data dictionary
    """

    user_data["watchlist"].append(movie)  

    return user_data

def watch_movie(user_data, title):
    """
    inputs: user_data (a dictionary with a "watchlist" and a "watched") and title (str)
    outputs: return user_data dict, which will be updated depending on whether the user has watched that title
    """
    #print(user_data)

    # if title is in watchlist, remove dictionary for that title from watchlist and add to watched list     
    for each_movie in user_data["watchlist"]:
        if each_movie["title"] == title:
            # add that dictionary to watched list
            user_data["watched"].append(each_movie)
            # remove dictionary from watchlist
            user_data["watchlist"].remove(each_movie)

    # return user_data in any case
    return(user_data)

#2============================================================================

def get_watched_avg_rating(user_data):
    """
    inputs: dictionary with a "watched" list of movie dictionaries 
    outputs: the average rating of all movies in the watched list
    """
    sum = 0
    
    # The average rating of an empty watched list is 0.0
    if not user_data["watched"]:
        return 0.0

    # add up all the ratings and divide by the number of ratings and store that value
    for each_movie in user_data["watched"]:
        sum += each_movie["rating"]
        average_rating = sum/len(user_data["watched"])

    # return the average rating (a float)
    return average_rating

# helper function to calculate mode:
def calc_mode_genre(genre_list):

    # create frequency map: a dictionary with key-value pairs of {'genre': frequency}
    genre_freq_dict = {}

    for genre in genre_list:
        if genre in genre_freq_dict.keys():
            genre_freq_dict[genre] += 1
        else:
            genre_freq_dict[genre] = 1

    # initialzing a placeholder for highest frequency
    highest_freq = 0
    most_pop_genre = 0

    # loop through frequency map dictionary
    for genre, genre_freq in genre_freq_dict.items():
        if genre_freq_dict[genre] > highest_freq:
            most_pop_genre = genre
            highest_freq = genre_freq 
            
    return most_pop_genre

def get_most_watched_genre(user_data):
    """
    input: that good ol dictionary with a watched list of movie dictionaries
    output: return the most popular genre (a string) 
    """
    genre_list = []

    # empty watched list returns None
    if not user_data["watched"]:
        return None 

    # else find the "genre" value that appears most frequently and return it
    for each_movie in user_data["watched"]:
        genre_list.append(each_movie["genre"])

    # return most popular genre string (the mode of the genre list)
    return calc_mode_genre(genre_list)
    
#3============================================================================

def get_unique_watched(user_data):
    """
    inputs: a dictionary of user's and friend's lists, where the friends lists contains unique dictionaries for each friend, which each contain a watched list of movie dictionaries
    outputs: a list of movie dictionaries unique to that user (a suggested watchlist to give to their friends) 
    """

    # initialize unique titles list for movie dictionaries 
    users_unique_movies = []
    friends_movies = []

    # should return an empty list if user's list is empty?
    if not user_data["watched"]:
        return []

    # add all friends watched movies to a new list
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)

    # for each movie in user's watched list
    for movie in user_data["watched"]:
        # check to see if the "title" value matches any in each friend's watched list, if not:
        if movie not in friends_movies:
            # add the DICTIONARY for the user's movie to unique titles list
            users_unique_movies.append(movie)

    # return a list of the movies the user has watched that their friends haven't seen yet
    return users_unique_movies

def get_friends_unique_watched(user_data):

    friends_unique_movies = []
    users_movies = []

    for movie in user_data["watched"]:
        users_movies.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in users_movies and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
            
    return friends_unique_movies

#4============================================================================

def get_available_recs(user_data):
    """
    inputs: the user_data dictionary
    outputs: a list of movie dictionaries that the user hasn't seen yet, is in their host network, and that at least one friend has seen; if no subscription data is gievn, it will just give movies the user hasn't seen and at least one friend has seen
    """

    recommended_movs = []
    users_movies = []
    
    for movie in user_data["watched"]:
        users_movies.append(movie)
        
    subscriptions_key = "subscriptions"

    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if movie not in recommended_movs:
    #             if subscriptions_key not in user_data:
    #                 recommended_movs.append(movie)
    #             elif movie["host"] in user_data["subscriptions"]:
    #                 recommended_movs.append(movie)    
    # return recommended_movs

    for friend in user_data["friends"]:
        if not friend["watched"]:
            return []
        else:
            for movie in friend["watched"]:
                if movie not in recommended_movs:
                    if subscriptions_key not in user_data:
                        recommended_movs.append(movie)
                    elif movie["host"] in user_data["subscriptions"]:
                        recommended_movs.append(movie)    
    return recommended_movs

#5============================================================================

def get_new_rec_by_genre(user_data):
    """
    inputs: user_data
    outputs: a list of movie recommendations (each one a dictionary), which are movies that the user has NOT watched (not present in "watched" list), and in their most watched genre, and is in at least ONE of their friend's "watched" lists 
    """
    
    movie_recs = []

    # a list of movie dictionaries that user hasn't seen, but at least one friend has seen
    unwatched_recs = get_available_recs(user_data) 

    # fave_genre is a str 
    fave_genre = get_most_watched_genre(user_data)

    for movie in unwatched_recs:
        if movie['genre'] == fave_genre:
            movie_recs.append(movie)
        else:
            continue 

    return movie_recs

def get_rec_from_favorites(user_data):
    """
    input: user_data
    output: a list of movies user can recommend to their friends (from user's favorites list but not in friend's watched list)
    """

    recommendations = []

    friends_watched_movs = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movs.append(movie)

    for movie in user_data["favorites"]:
        if movie not in friends_watched_movs:
            recommendations.append(movie)

    return recommendations