# Wave 1 s
def create_movie(movie_title,genre,rating):
    movie = {}
    if movie_title == None or genre == None or rating == None:
        return None
    else: 
        movie["title"] = movie_title
        movie["genre"] = genre
        movie["rating"] = rating
    print(movie)
    return movie

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return(user_data)

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return(user_data)

def watch_movie(user_data, movie):
    for elem in user_data['watchlist']:
        if movie == elem['title']:
            user_data['watchlist'].remove(elem)
            user_data['watched'].append(elem)
    return user_data 

# Wave 2   
def get_watched_avg_rating(user_data):
    sum = 0.0
    avg = 0.0
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            sum+=movie["rating"]
            print(sum)
        avg = sum/len(user_data["watched"]) 
        return(avg)
    else:
        return 0

def get_most_watched_genre(user_data):
    genre_dict = {}
    if len(user_data) == 0 or len(user_data["watched"]) == 0:
        return None
    else: 
        for movie in user_data["watched"]:
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] +=1
            else:
                genre_dict[movie["genre"]] = 1
    maximum = max(genre_dict, key=genre_dict.get) 
    return(maximum)

# Wave 3
def get_unique_watched(user_data):
    user_set = set()
    friend_set = set()

    for user_movies in user_data["watched"]:
        user_set.add(user_movies["title"])
        
    for friend_items in user_data["friends"]:
            for movie in friend_items["watched"]:
                for title,val in movie.items():
                    friend_set.add(val)
    unique_set = user_set - friend_set
    
    unique_list = []
    for movie in unique_set:
        x = dict(title = movie)
        unique_list.append(x)
    return(unique_list)

def get_friends_unique_watched(user_data):
    user_list = []
    friend_list = []
    friend_unique_list = []

    for user_movies in user_data["watched"]:
        user_list.append(user_movies)
        
    for friend_items in user_data["friends"]:
            for movie in friend_items["watched"]:
                    friend_list.append(movie)

    for movie in friend_list:
        if movie not in user_list and movie not in friend_unique_list:
            friend_unique_list.append(movie)
    return(friend_unique_list)

# Wave 4
def get_available_recs(user_data):
    recommended_movies = []

    subs = user_data["subscriptions"]
    for friend_items in user_data["friends"]:
            for movie in friend_items["watched"]:
                if movie["host"] in subs and movie not in recommended_movies:
                    recommended_movies.append(movie)
    return(recommended_movies)

# Wave 5

def get_new_rec_by_genre(user_data):
    recommendations_list = []
    friends_movies_list = get_friends_unique_watched(user_data)

    if not user_data["watched"]:
        user_genres_list = []
    else:
        user_genres_list = get_most_watched_genre(user_data)  

    for movie in friends_movies_list:
        if movie["genre"] in user_genres_list:
            recommendations_list.append(movie)
    return(recommendations_list)

def get_rec_from_favorites(user_data):
    user_favs = user_data["favorites"]
    friend_watched_movies = {}
    recommended_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_movies[movie["title"]] = True
    for fav in user_favs:
        if fav["title"] not in friend_watched_movies:
            recommended_movies.append(fav)
    return(recommended_movies)