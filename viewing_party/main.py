#************** WAVE 1 ***************

def create_movie(title, genre, rating):
    
    new_movie = {}
    
    if type(title) == str and type(genre) == str and type(rating) == float:
        new_movie["title"] = title 
        new_movie["genre"] = genre
        new_movie["rating"] = rating

        return new_movie

    else: 
        return None


def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched_list = user_data["watched"]

    for movie in watchlist:

        if title == movie["title"]:
            watchlist.remove(movie)
            watched_list.append(movie)
    return user_data

# #************** WAVE 2 ***************

def get_watched_avg_rating(user_data):
    rating_list = []
    
    for movie in user_data["watched"]:
        rating_list.append(movie["rating"])

    thesum = sum(rating_list)
    avg_rating = thesum/(len(rating_list))

    return avg_rating

def get_watched_avg_rating(user_data):
    sum = 0.0
    count = 0

    try:
        for movie in user_data["watched"]:
            sum += movie["rating"]
            count += 1
        avg_rating = sum/count

    except ZeroDivisionError:
        avg_rating = 0.0
    
    return float(avg_rating)

def get_most_watched_genre(user_data):
    #grab all the genres and put into watched_genre_list
    watched_genre_list = []
    genre_count = {}
    # most_watched_genre = []
    current_max = 0

    if not user_data["watched"]:
        return None

    else:
        for movie in user_data["watched"]:
            watched_genre_list.append(movie["genre"])
    
    #go through list and count occurences of each genre. store this as key:value pairs in genre_count dictionary
    
        for genre in watched_genre_list: 
            if genre in genre_count:
                genre_count[genre] = genre_count[genre] +1
            else:
                genre_count[genre] = 1

#  #go through genre_count dictionary and add all the genres with the highest counts into the most_watched_genre list. 

        for val in genre_count.values():
            if val >= current_max:
                current_max = val
    
        for key, values in genre_count.items():
            if values == current_max:
                winner = key
            # most_watched_genre.append(key)

        return winner

#************** WAVE 3 ****************

def create_friends_titles_list(user_data):
    friend_list = user_data["friends"]

    friends_titles_list = []

    for watched_dict in friend_list: 
        dict_in_friend_list = watched_dict
        #list of two dictionaries with key["watched"], value is list of dictionaries
        for movie_dict in dict_in_friend_list["watched"]:
            movie_dict_copy = movie_dict.copy()
            friends_titles_list.append(movie_dict_copy)

    return friends_titles_list


def get_unique_watched(user_data):
    my_watched_list = []

    for movie in user_data["watched"]:
        my_watched_list.append(movie)
    
    friends_titles_list = create_friends_titles_list(user_data)

    unique_list = []

    #compare and make list of dictionaries of unique values

    for item in my_watched_list:
        if item not in friends_titles_list:
            unique_list.append(item)


    return unique_list

def get_friends_unique_watched(user_data):
    
    my_watched_list = []

    for movie in user_data["watched"]:
        my_watched_list.append(movie)

    friends_titles_list = create_friends_titles_list(user_data)
    #friends_titles_list has all the titles that friends have watched

    friends_watched_list = []

    #make list of dictionaries of unique values

    for item in friends_titles_list:
        if item not in my_watched_list:
            if item in friends_watched_list:
                continue 
            friends_watched_list.append(item)

    return friends_watched_list

#************** WAVE 4 ****************

def get_available_recs(user_data):
    list_of_recs = get_friends_unique_watched(user_data)
    my_subs_list = user_data["subscriptions"]
    friends_watched_list = user_data["friends"]


    available_recs = []

    for friend in friends_watched_list:
        for movie_dict in friend["watched"]:
            if movie_dict["host"] in my_subs_list:
                for rec in list_of_recs:
                    if movie_dict["title"] in rec["title"]:
                        rec_copy = movie_dict.copy()
                        if rec_copy in available_recs:
                            continue
                        available_recs.append(rec_copy)

    return available_recs

#************** WAVE 5 ****************

def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)

    list_of_recs = get_friends_unique_watched(user_data)

    rec_by_genre = []

    if most_watched_genre is None:
        rec_by_genre is None

    else:
        for movie in list_of_recs:
            if most_watched_genre == movie["genre"]:
                genre_rec_copy = movie.copy()
                if genre_rec_copy in rec_by_genre:
                    continue
                rec_by_genre.append(genre_rec_copy)

    return rec_by_genre

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    user_favorites = user_data["favorites"]

    movie_recs = []

    for fav_movie in user_favorites:
        if fav_movie in unique_watched:
            fav_movie_copy = fav_movie.copy()
        if fav_movie_copy in movie_recs:
            continue
        movie_recs.append(fav_movie_copy)

    return movie_recs


