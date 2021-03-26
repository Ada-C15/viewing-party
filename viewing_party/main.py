# Project 1 - Viewing party
# Katrina Kimzey (she|they)
# Ada Cohort 15 - paper class
# Started: March 17, 2021
# Last Updated: March 26, 2021


# WAVE ONE 
# =====================================================================

def create_movie(title, genre, rating):
    # builds a dictionary with all info
    # If no movie title/genre/rating given, return None
    if title and genre and rating:
        return {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
    else:
        return None

def add_to_watched(user_watched_list, movie):
    # update watched list to include given movie
    # movie is a dictionary
    # user_watched_list is a dict
    user_watched_list["watched"].append(movie)
    return user_watched_list

def add_to_watchlist(user_to_watchlist, movie):
    # update list (inside dict) to watch with given movie
    user_to_watchlist["watchlist"].append(movie)
    return user_to_watchlist

def watch_movie(user, movie_title):
    # move from to watch list to watched list
    # user is a dictionary
    # movie is a str
    # DO NOTHING if movie is not in to watch list
    for film in user["watchlist"]:
        if film["title"] == movie_title:
            add_to_watched(user, film)
            user["watchlist"].remove(film)
    
    return user


# WAVE TWO
# =====================================================================

def get_watched_avg_rating(user_data):
    if not len(user_data["watched"]):
        return 0

    ratings_sum = 0.0

    for each in user_data["watched"]:
        print(each["rating"])
        ratings_sum += each["rating"]

    return ratings_sum/len(user_data["watched"])

def get_most_watched_genre(user_data):
    # frequency dictionary of genres
    g_frequency = {}

    # counts each time the genre shows up
    for each in user_data["watched"]:
        if each["genre"] in g_frequency:
            g_frequency[each["genre"]] += 1
        else:
            g_frequency[each["genre"]] = 1

    # compares the frequency to find the most watched
    genre_popular = None

    for i in g_frequency:
        if not genre_popular:
            genre_popular = i
        elif g_frequency[genre_popular] < g_frequency[i]:
            genre_popular = i

    return genre_popular

# WAVE 3
# =====================================================================

def get_unique_watched(user_data):
    # return a list of all the movies user has seen that friends have not
    unique_films = user_data["watched"]

    for friend in user_data["friends"]:
        for movie in unique_films:
            for film in friend["watched"]:
                if movie["title"] == film["title"]:
                    unique_films.remove(movie)
    
    return unique_films

def get_friends_unique_watched(user_data):
    # return a list of all movies friend's have seen that user has not
    unique_films = [films for friend in user_data["friends"] for films in friend["watched"]]

    for movie in user_data["watched"]:
        for film in unique_films:
            if movie["title"] == film["title"]:
                unique_films.remove(film)

    i = 0
    while i < len(unique_films):
        if i == 0:
            i += 1
            continue
        for j in range(i):
            if unique_films[i]["title"] == unique_films[j]["title"]:
                del unique_films[j]
        i += 1

    return unique_films

# WAVE 4
# =====================================================================

def get_available_recs(user_data):
    # get movies that friends have watched and are on a service the user has
    unseen_friend_recs = get_friends_unique_watched(user_data)
    available_recs = []

    for film in unseen_friend_recs:
        for service in user_data["subscriptions"]:
            if service == film["host"]:
                available_recs.append(film)
    
    return available_recs

# WAVE 5
# =====================================================================

def get_new_rec_by_genre(user_data):
    # most popular genre recommendation from friends' lists
    friends_recs = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)
    genre_recs = []

    for film in friends_recs:
        if film["genre"] == favorite_genre:
            genre_recs.append(film)

    return genre_recs

def get_rec_from_favorites(user_data):
    # recommend from user's favs that friends haven't seen
    user_recs = get_unique_watched(user_data)
    recs_for_friends = []

    for film in user_recs:
        for movie in user_data["favorites"]:
            if movie["title"] == film["title"]:
                recs_for_friends.append(movie)

    return recs_for_friends
