### --------------- WAVE 1 --------------- ###

def create_movie(movie_title, genre, rating):
    # take in three parameters title, genre, rating
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating":  rating
    }
    # if title, genre, OR rating is falsy, return None
    for values in new_movie.values():
        if values == None:
            return None
    # step 3: if the attributes are truthy, return dictionary
    else:
        return new_movie


def add_to_watched(user_data, movie):
    # access the value of "watched" list and assign variable
    watched_list = user_data["watched"]

    # append movie to "watched" list
    watched_list.append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    # just repeat what you did in add_to_watched
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    # iterate thru the movies in "watchlist" list
    for movie in user_data['watchlist']:
        # check if the value of movie["title"] matches the paremeter title 
        if title == movie['title']:
            # then add to "watched" list and remove from "watchedlist" list
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
    return user_data

### --------------- WAVE 2 --------------- ###

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    rating_list = []

    # loop to make list that captures only the ratings
    for movie in watched_list:
        rating_list.append(movie["rating"])
    # handle for zero division error
    if len(rating_list) == 0:
        avg_rating = 0.0
        return avg_rating
    else:
        avg_rating = sum(rating_list)/len(rating_list)
        return avg_rating

def calculate_genre_freq(user_data):
    '''
    helper function to calculate genre frequency
    '''

    # dictionary where the keys are the genre "fanatasy"
    genre_freq_dict = {}
    watch_list = user_data["watched"]

    for movie in watch_list: 
        genre = movie["genre"]
        # go thru watch_list and check if that genre is arleady a key 
        # if its already in dictionary add 1 to it  
        if genre in genre_freq_dict.keys(): 
            genre_freq_dict[genre] += 1 
        else: 
            genre_freq_dict[genre] = 1
    return genre_freq_dict

def get_most_watched_genre(user_data):
    #call calculate_genre_freq to get genre_freq_dict
    genre_freq_dict = calculate_genre_freq(user_data)
    #initalize highest to 0
    highest = 0
    most_watched_genre = None
    #iterate through the genre_freq_dict
    for genre, freq in genre_freq_dict.items(): 
    #check if the value  (genre_freq_dict[genre]) is higher than the current value stored in highest
        if freq > highest:  #value int
            # if it is assign highest_genre to current genre
            # and replace highest with the freq
            highest = freq #value int
            most_watched_genre = genre
    return most_watched_genre


### --------------- WAVE 3 --------------- ###

def get_unique_watched(user_data):

    user_movies = user_data["watched"]  # list of the movies (dict)
    friends_list = user_data["friends"] # list of dict

    # make a set for user watched and friend watched
    user_set = set()
    friend_set = set()

    for watched_dict in friends_list:
        for movie in watched_dict["watched"]:
            friend_set.add(movie["title"])

    for movie in user_movies:
        user_set.add(movie["title"])

    # compare the sets to find the movies the user has watched but the friend hasnt
    user_unique_movies_set = user_set.difference(friend_set)

    # put the movies into a list of dictionaries (each dict is movie)
    user_unique_movies_list = []
    for movie_name in user_unique_movies_set:
        movie = dict(title=movie_name)
        user_unique_movies_list.append(movie)
    return user_unique_movies_list


def get_friends_unique_watched(user_data):
    # initiate empty list to capture friend's unique movies 
    unique_movies = []
    # iterate through the "friends" lists of dictionaries 
    for friends_watched in user_data["friends"]:
        # iterate through the movies in "watched" dictionary
        for movie in friends_watched["watched"]:
            # check if movie is not in "watched" list and not already in unique_movies list 
            if movie not in user_data["watched"] and movie not in unique_movies:
                unique_movies.append(movie)
    return unique_movies

### --------------- WAVE 4 --------------- ###

def get_available_recs(user_data):
    # call get_friends_unique_watched to use as helper function
    unique_movies = get_friends_unique_watched(user_data)
    # recommended movies are the unique ones that have a host in the users subscription list
    recommended_movies = []
    
    # iterate thru unique_movies
    for movie in unique_movies:
        # append to recommended movies if the movie ["host"] is in user_data["subscriptions"]
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

### --------------- WAVE 5 --------------- ###

def get_new_rec_by_genre(user_data):
    # invoke functions to get friends unique movies and users fav genre
    friends_unique_movies = get_friends_unique_watched(user_data)
    users_favorite_genre = get_most_watched_genre(user_data)

    # determine list of recommended movies
    recommended_movies_genre = []
    for movie in friends_unique_movies:
        if movie["genre"] == users_favorite_genre:
            recommended_movies_genre.append(movie)
    return recommended_movies_genre


def get_rec_from_favorites(user_data):

    # make an empty set for friends watched movies 
    friends_watched_movies = set()
    recs = []
    for friend in user_data["friends"]: 
        for movie in friend["watched"]: 
            friends_watched_movies.add(movie["title"])
        
    # list of users favorites 
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_watched_movies: 
            recs.append(movie)
    return recs