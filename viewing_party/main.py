# WAVE ONE  

def create_movie(title, genre, rating):
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if title == None or genre == None or rating == None:
        return None 
    return movie_dict



def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data 



def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data



def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data



# WAVE TWO 

    # PROBLEM ONE 
    # I need to calculate the total sum of the ratings
    # Then I need to divide the total sum by the length of the movies in the watched list 
def get_watched_avg_rating(user_data):
    sum_counter = 0
    for movie in user_data["watched"]:
        sum_counter += movie["rating"] 
    if len(user_data["watched"]) == 0:
        return 0.0 

    average_rating = sum_counter/len(user_data["watched"])
    return average_rating 

    # PROBLEM TWO 
    # iterating through the watched list
    # each loop gives us one movie 
    # get genre from movie 
    # add new genre into the dictionary as a key with count being the value, (check if genre is in the dict and add one) OR (add too dict at 1)
    # Now iterate over different_genre dict
    # Find highest value  
    # return key to highest value 
def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    genres = {}
    for movie in user_data["watched"]:
        for i, x in movie.items():
            if i == "genre":
                if x in genres:
                    genres[x] += 1 
                else:
                    genres[x] = 1

    count = 0
    most_watched = ""

    for i, x in genres.items():
        if x > count:
            count = x
            most_watched = i 
        
    return most_watched




# WAVE THREE 

    # PROBLEM ONE 
def get_unique_watched(user_data):
    unique_movies = []
    have_seen = {}
    friends = user_data["friends"] # list of friends 
    for movie in user_data["watched"]:
        have_seen[movie["title"]] = False 
    
    for friend in friends:
        friend_seen_list = friend["watched"]
        for friend_movie in friend_seen_list:
            friend_movie_title = friend_movie["title"]
            if friend_movie_title in have_seen:
                have_seen[friend_movie_title] = True

    for movie in user_data["watched"]:
        if not have_seen[movie["title"]]:
            unique_movies.append(movie)

    return unique_movies 


    # PROBLEM TWO
    # make an empty list user_has_not_seen_but_friends_have
    # I need to iterate through the user watched list and compare the list to the movies that their friends have watched and identify which movies have been not been seen by the user
    # add those unseen movies to the empty list user_has_not_seen_but_friends_have
    # then return user_has_not_seen_but_friends_have
def get_friends_unique_watched(user_data):
    user_has_not_seen_but_friends_have = []
    user_has_seen = user_data["watched"]
    friends = user_data["friends"]
    have_seen = {}

    for friend in friends:
        friend_seen_list = friend["watched"]
        for friend_movie in friend_seen_list:
            friend_movie_title = friend_movie["title"]
            have_seen[friend_movie_title] = False 
    for movie in user_has_seen:
        if movie["title"] in have_seen:
            have_seen[movie["title"]] = True 

    for friend in friends:
        friend_seen_list = friend["watched"]
        for friend_movie in friend_seen_list:
            if not have_seen[friend_movie["title"]]:
                user_has_not_seen_but_friends_have.append(friend_movie)
                have_seen[friend_movie["title"]] = True 


    return user_has_not_seen_but_friends_have




# WAVE FOUR 

    # PROBLEM ONE
    # create an empty list recommended_movies
    # iterate through each movie in the friends watched list and add that movied to the recommended_movies IF the user has not watched it AND at least one of the friends has seen it AND the "host" of the movie is a service that is in the users "subscriptions"
    # return the list recommended_movies 
    # check to see if the "host" in the movie dict matches a 'host' in the user_data subscriptions list 
def get_available_recs(user_data):
    recommended_movies = []
    unique_movies = get_friends_unique_watched(user_data)
    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies 
    


# WAVE FIVE 

    # PROBLEM ONE 
    # find users most common genre
    # create empty list users_most_common_genre_recs 
    # iterate through each movie in the friends watched list and add to the users_most_common_genre_recs IF the user has not watched it AND at least one of the users friends has watched it AND the genre of the movie is the same as the users most frequent genre
    # then return users_most_common_genre_recs
def get_new_rec_by_genre(user_data):
    users_most_common_genre_recs = []
    number_one_genre = get_most_watched_genre(user_data)
    unique_movies = get_friends_unique_watched(user_data)
    for movie in unique_movies:
        if movie["genre"] == number_one_genre:
            users_most_common_genre_recs.append(movie)

    return users_most_common_genre_recs

    # PROBLEM TWO
    # create an empty list recommended_by_favorites  
    # use the users most frequently watched genre and then add each one of those matching genres into the recommended_by_favorites list ONLY IF the movie is in the users favorites AND non of the users friends have watched it
    # make a list of our favorites based off fav genre
    # go through friends watched list 
    # return recommended_by_favorites 
def get_rec_from_favorites(user_data):
    recommended_by_favorites = user_data["favorites"]
    
    for friend in user_data["friends"]:
        friend_seen_list = friend["watched"]
        for friend_movie in friend_seen_list:
            if friend_movie in user_data["favorites"]:
                recommended_by_favorites.remove(friend_movie)

    return recommended_by_favorites