# WAVE ONE

def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    
    movie = {}
    movie['title'] = movie_title
    movie['genre'] = genre
    movie['rating'] = rating
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# moves movie from watchlist to watched list in user_data
def watch_movie(user_data, movie_title):
    for movie in user_data['watchlist']:
        if movie['title'] == movie_title:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
            return user_data
    else:
        return user_data


# WAVE TWO

def get_watched_avg_rating(user_data):
    if len(user_data['watched']) > 0:
        sum = 0
        for movie in user_data['watched']:
            sum += movie['rating']
        return sum / len(user_data['watched'])
    else:
        return 0

def get_most_watched_genre(user_data):
    genres = {}
    if len(user_data['watched']) == 0:
        return None
    for movie in user_data['watched']:
        if movie['genre'] in genres:
            genres[movie['genre']] += 1
        else:
            genres[movie['genre']] = 1
    
    max_value = max(genres.values())

    for genre in genres:
        if genres[genre] == max_value:
            return genre


# WAVE THREE

def get_unique_watched(user_data):
    # make a unique movies list, initialized to empty
    unique_movies = []
    # make a list of movies that user has watched
    user_watched_list = make_user_watched_list(user_data)
    # make a list of movies that friends have watched
    friends_watched_list = make_friends_watched_list(user_data)
    # loop through amanda's watched lists
    for movie in user_watched_list:
        # if there's a movie that does not appear in friend's watched lsits,
        if movie not in friends_watched_list:
            unique_movies.append(movie)
    
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []

    user_watched_list = make_user_watched_list(user_data)
    friends_watched_list = make_friends_watched_list(user_data)

    for movie in friends_watched_list:

        if movie not in user_watched_list:
            friends_unique_movies.append(movie)
    
    return friends_unique_movies

# helper function
def make_user_watched_list(user_data):
    user_watched_list = []
    for movie in user_data['watched']:
        user_watched_list.append(movie)
    return user_watched_list

# helper function
def make_friends_watched_list(user_data):
    friends_watched_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    return friends_watched_list


# WAVE FOUR

def get_available_recs(user_data):
    rec_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie['host'] in user_data['subscriptions']:
                if movie not in rec_list:
                    rec_list.append(movie)
    return rec_list


# WAVE FIVE

def get_new_rec_by_genre(user_data):
    rec_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if (movie not in user_data['watched']) and (len(user_data['watched']) > 0):
                if movie not in rec_list:
                    rec_list.append(movie)
    return rec_list

# gets a recommendation for user's friends based upon overlap of user's favorites and movies friends have not seen
def get_rec_from_favorites(user_data):
    rec_list = user_data['favorites']
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie in rec_list:
                rec_list.remove(movie)
    return rec_list
