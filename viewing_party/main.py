####################### Wave_01 #########################
#Creat new movie with three attributes movie_title, genre and rating
def create_movie(movie_title, genre, rating):
    new_movie = {}
    if movie_title and genre and rating:
        new_movie["title"] = movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None

#Add movie information to user watched list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#Add movie information to user watchlist  
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#Add movie from watchlist to watched
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

####################### Wave_02 #########################
#Calculate average rating of movies in users watched list
def get_watched_avg_rating(user_data):  
    ratings = 0
    cnt = len(user_data["watched"])
    if cnt > 0:
        for movie in user_data["watched"]:
            ratings += movie["rating"]
        return ratings/cnt
    else:
        return 0

#Find the most frequently watched genre in users watched list
def get_most_watched_genre(user_data):
    most_watched = {}
    max_cnt = 0
    genre = ""
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in user_data["watched"]:
            if movie["genre"] in most_watched:
                most_watched[movie["genre"]] += 1
                if most_watched[movie["genre"]] > max_cnt:
                    max_cnt = most_watched[movie["genre"]]
                    genre = movie["genre"]
            else:
                most_watched[movie["genre"]] = 1
    return genre

####################### Wave_03 #########################
###### Helper function to make a set of user_watched movie ######
def get_user_watched(user_data):
    user_watched = set()
    for movie in user_data["watched"]:
        user_watched.add(movie["title"])
    return user_watched
  
###### Helper function to make a set of friend_watched movie ######  
def get_friends_watched(user_data):
    friend_watched = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.add(movie["title"])
    return friend_watched
  
#Find movies which have only been watched by the user  
def get_unique_watched(user_data):
    difference = get_user_watched(user_data) - get_friends_watched(user_data)
    user_unique_watched = []
    for movie in difference:
        user_unique_watched.append({"title": movie})
    return user_unique_watched
  
#Find movies which have only been watched by users friends
def get_friends_unique_watched(user_data):
    difference = get_friends_watched(user_data) - get_user_watched(user_data)
    friends_unique_watched = []
    for movie in difference:
        friends_unique_watched.append({"title": movie})
    return friends_unique_watched                     

####################### Wave_04 #########################
#Get movie recommendations based on users subscription
def get_available_recs(user_data):
    user_sub = set(user_data["subscriptions"])
    added = set()
    recommendation = []
    user_watched = get_user_watched(user_data)
    for friend in user_data["friends"]:
        for movie in friend["watched"]: 
          if movie["host"] in user_sub:
              if movie["title"] not in user_watched and movie["title"] not in added:
                  added.add(movie["title"])
                  recommendation.append(movie)
    return recommendation
  
####################### Wave_05 #########################
#Get movie recommendations based on users most watched genre
def get_new_rec_by_genre(user_data):
    recommendation = []
    most_watched = get_most_watched_genre(user_data)
    for friend in user_data["friends"]:
        for movie in friend["watched"]: 
            if movie not in user_data["watched"] and movie["genre"] == most_watched:
                recommendation.append(movie)
    return recommendation
  
#Get movie recommendations based on users favourite movie
def get_rec_from_favorites(user_data):
    recommendation = []
    friend_watched = get_friends_watched(user_data)
    for movie in user_data["favorites"]:
        if movie["title"] not in friend_watched:
            recommendation.append(movie)
    return recommendation
    
