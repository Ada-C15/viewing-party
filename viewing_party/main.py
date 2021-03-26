def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title 
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie

    else:
        return None
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data['watchlist']
    for movie in watchlist:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data
        

#WAVE_2-------------------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    average = 0.0
    if len(user_data["watched"]) == 0:
        return average 
    for movie in user_data["watched"]:
        sum = sum + movie["rating"]
        average = sum / len(user_data["watched"])
    return average
def get_most_watched_genre(user_data):
    most_watched = user_data['watched']
    popular_genre = {}
    
    for movie in most_watched:
        genre = movie["genre"]
        if genre in popular_genre:
            popular_genre[genre] += 1
        else:
            popular_genre[genre] = 1 

    max = 0
    max_genre = None
    for genre,count in popular_genre.items():
        if count > max: 
            max = count
            max_genre = genre
    return max_genre

#WAVE_3----------------------------------------------------------
def make_friends_list(user_data):
    friends_list = []
    for friend in user_data["friends"]:
        for movie in friend['watched']:
            friends_list.append(movie)
    return friends_list
# friends list

def get_unique_watched(user_data):
    friends_list = make_friends_list(user_data)
    
    movie_list = []
    for user_movie in user_data["watched"]:
        if user_movie not in friends_list:
            movie_list.append(user_movie)
    return movie_list
    #return friends_list
def get_friends_unique_watched(user_data):
    friends_list = make_friends_list(user_data)
    user_unwatched = []
    for unwatched in friends_list:
        if unwatched not in user_data['watched'] and unwatched not in user_unwatched: 
            user_unwatched.append(unwatched)
    return user_unwatched
#Wave_4-----------------------------------------------------
#def user_unwatched_help():


def get_available_recs(user_data):
    recommended_movies = []
    friend_list = []

    for movie in user_data["friends"]:
        for host in movie["watched"]:
            friend_list.append(host)
    for movie in friend_list:
        if movie not in user_data["watched"] and movie not in recommended_movies and movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies
#------------------------------------------------------------


def get_new_rec_by_genre(user_data):

    recommended_movies = []
    fav_genre = get_most_watched_genre(user_data)

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["genre"] == fav_genre and friend_movie \
                not in user_data["watched"] and friend_movie not in recommended_movies:
                recommended_movies.append(friend_movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    # movies our friends haven't watched that are user favs
    recommended_movies = user_data['favorites']

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie in user_data['favorites']:
                recommended_movies.remove(friend_movie)
    return recommended_movies