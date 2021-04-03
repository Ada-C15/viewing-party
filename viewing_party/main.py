
#the functions below are for wave_01
# 

def create_movie(movie_title,  genre, rating):
    if not movie_title or not genre or not rating:
        return None
    return {
        "title":  movie_title, 
        "genre" : genre,
        "rating" :rating 
        }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

  
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    watched_movie = {}
    watchlist = user_data["watchlist"]
    for index in range(len(watchlist)):
        if watchlist[index]["title"] == movie:
            watched_movie = watchlist[index]
            watchlist.pop(index)
            return add_to_watched(user_data, watched_movie)
    return user_data

#the functions below are for wave_02 
def get_watched_avg_rating (user_data):
    sum = 0 
    watched = user_data["watched"]
    if watched:
       for movie in watched:
          sum += watched["rating"]
        sum = sum / len(watched)
     return sum


def get_most_watched_genre(user_data):
    genres = {}
    most_watched = {}
    watched = user_data["watched"]
    if len(watched)== 0:
        return None
    for index in range(len(watched)):
        genre = watched[index]["genre"]
        if genres.get(genre):
            genres[genre] +=1 
        else: genres[genre] = 1
    key = list(genres.keys())[0]
    value = list(genres.values())[0]
    most_watched[key] = value
  
    for genre in genres:
        if genres[genre] > list(most_watched.values())[0]:
            most_watched.clear()
            most_watched[genre] = genres[genre]
        elif genres[genre] == list(most_watched.values())[0]:
             most_watched[genre] = genres[genre]
    return ", ".join(list(most_watched.keys()))


# wave 3

def get_unique_watched(user_data):
    movies_watched_by_user = {}
    watched = user_data["watched"]
    for index in range(len(watched)):
        movies_watched_by_user[watched[index]["title"]] = watched[index]
    for index in range(len(user_data["friends"])):
        friend_watched = user_data["friends"][index]["watched"]
        for index in range(len(friend_watched)):
            if movies_watched_by_user.get(friend_watched[index]["title"]):
                movies_watched_by_user.pop(friend_watched[index]["title"], None)
    return list(movies_watched_by_user.values())


def get_friends_unique_watched(user_data):
    movies_watched_by_user = {}
    movies_watched_by_friend = {}

    watched = user_data["watched"]
    for index in range(len(watched)):
        movies_watched_by_user[watched[index]["title"]] = watched[index]
    for index in range(len(user_data["friends"])):
        friend_watched = user_data["friends"][index]["watched"]
        for index in range(len(friend_watched)):
            if not movies_watched_by_user.get(friend_watched[index]["title"]):
                movies_watched_by_friend[friend_watched[index]["title"]] = friend_watched[index]
    return list(movies_watched_by_friend.values())




# Wave 4 here we go! 
def get_available_recs(user_data):
    movie_recs = []
    friends_watched = get_friends_unique_watched(user_data)

    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie) 
    
    return movie_recs    

# Wave 5 here we go

def get_new_rec_by_genre(user_data):
    movie_recs = []
    friends_watched = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)

    for movie in friends_watched:
        if movie["genre"] == favorite_genre:
            movie_recs.append(movie) 
    
    return movie_recs   


def get_rec_from_favorites(user_data):
  
    user_data["watched"] = user_data["favorites"]
    user_watched = get_unique_watched(user_data)

    return user_watched
