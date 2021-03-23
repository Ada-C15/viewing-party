def create_movie(movie_title, genre, rating):
    new_movie = {
        "title" : 0,
        "genre" : 0,
        "rating": 0
    }
    if movie_title == None:
        new_movie = None
        return None
    else: 
        new_movie["title"] = movie_title

    if genre == None:
        new_movie = None
        return None
    else:
        new_movie["genre"] = genre

    if rating == None:
        new_movie = None
        return None
    else:
        new_movie["rating"] = rating
    print(new_movie)
    return new_movie

def add_to_watched(user_data, movie):
    list = user_data["watched"]
    list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            user_data["watched"].append(movie)
            return user_data
    else:
        return user_data

#################################################

def get_watched_avg_rating(user_data):
    nums_to_avg = []
    sum = 0
    watched = user_data["watched"]
    for movie in watched:
        if movie["rating"] >= 0:
            nums_to_avg.append(movie["rating"])
            sum = sum + movie["rating"]
    if len(nums_to_avg) == 0:
        return 0.0
    average = sum / len(nums_to_avg)
    return average
    
def get_most_watched_genre(user_data):
    genre_count = {}
    most_watched_genre = None
    most_watched_genre_count = 0 
    watched = user_data["watched"]
    for movie in watched:
        genre = movie["genre"]
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] = genre_count[genre] + 1
    for genre, count in genre_count.items():
        if count > most_watched_genre_count:
            most_watched_genre_count = count
            most_watched_genre = genre        
    return most_watched_genre

########################################################################

def get_unique_watched(user_data):
    unique_movies = []
    user_watched_by_title = {}
    watched = user_data["watched"]
    for movie in watched:
        user_watched_by_title[movie["title"]] = movie
    #print(user_watched_by_title)
    friends = user_data["friends"]
    for friend in friends:
        friend_watched = friend["watched"]
        for movie in friend_watched: 
            user_watched_by_title.pop(movie["title"], None)
    unique_movies.extend(user_watched_by_title.values())
    #print(unique_movies)
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friends_watched_by_title = {}
    friends = user_data["friends"]
    for friend in friends:
        friend_watched = friend["watched"]
        for movie in friend_watched:
            friends_watched_by_title[movie["title"]] = movie
    #print(friends_watched_by_title)
    watched = user_data["watched"]
    for movie in watched:
        friends_watched_by_title.pop(movie["title"], None)
    friends_unique_movies.extend(friends_watched_by_title.values())
    #print(friends_unique_movies)
    return friends_unique_movies

######################################################################

def get_available_recs(user_data):
    recommendations = []
    recommended_movies = {}
    subscriptions = user_data["subscriptions"]
    friends = user_data["friends"]
    for friend in friends:
        friend_watched = friend["watched"]
        for movie in friend_watched:
            if movie["host"] in subscriptions:
                recommended_movies[movie["title"]] = movie
    watched = user_data["watched"]
    for movie in watched:
        recommended_movies.pop(movie["title"])
    recommendations.extend(recommended_movies.values())
    return recommendations

#######################################################################

def get_new_rec_by_genre(user_data):
    recommendations = []
    recommended_by_genre = {}
    genre = get_most_watched_genre(user_data)
    friends = user_data["friends"]
    for friend in friends:
        friend_watched = friend["watched"]
        for movie in friend_watched:
            if movie["genre"] == genre:
                recommended_by_genre[movie["title"]] = movie
    watched = user_data["watched"]
    for movie in watched:
        recommended_by_genre.pop(movie["title"], None)
    recommendations.extend(recommended_by_genre.values())
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    favorite_movies = {}
    favorites = user_data["favorites"]
    for movie in favorites:
        favorite_movies[movie["title"]] = movie
    friends = user_data["friends"]
    for friend in friends:
        friend_watched = friend["watched"]
        for movie in friend_watched:
            favorite_movies.pop(movie["title"], None)
    recommendations.extend(favorite_movies.values())
    return recommendations