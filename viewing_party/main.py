def create_movie(title, genre, rating):
    movie_dict = {"title": title, "genre": genre, "rating": rating}
    if None in movie_dict.values():
      return None
    else: 
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

def list_com_fun(user_data_user_data_key, value):
    list_com = [v for i in user_data_user_data_key for k,v in i.items() \
        if v == i[value]]
    return list_com
    
def get_watched_avg_rating(user_data):
    list_dic = user_data["watched"]
    avg_rating = 0.0    
    if len(list_dic) > 0:
        rating_list = [v for i in list_dic for k,v in i.items() if k=="rating"]
        avg_rating = sum(rating_list) / len(rating_list)
        return avg_rating
    else:
        return avg_rating

def get_most_watched_genre(user_data):
    genres = list_com_fun(user_data["watched"], "genre")
    if genres == []:
        return None
    return max(genres)
    
def get_unique_watched(user_data):
    answer = []
    user = list_com_fun(user_data["watched"], "title")
    friend1 = list_com_fun(user_data["friends"][0]["watched"] , "title") 
    friend2 = list_com_fun(user_data["friends"][1]["watched"] ,"title")
    friend_movies = friend1 + friend2
    unique = [x for x in user if x not in friend_movies]
    for v in unique:
        movie = {"title":v}
        movie_copy = movie.copy()
        answer.append(movie_copy)
    return answer 
    
def get_friends_unique_watched(user_data):
    answer = []
    user = list_com_fun(user_data["watched"],"title")
    friend1 = list_com_fun(user_data["friends"][0]["watched"],"title")
    friend2 = list_com_fun(user_data["friends"][1]["watched"] ,"title")
    friend_movies = friend1 + friend2
    unique = [x for x in friend_movies if x not in user]
    unique = set(unique)
    for v in unique:
        movie = {"title":v}
        movie_copy = movie.copy()
        answer.append(movie_copy)
    return answer

def get_available_recs(user_data):
    user_sub = user_data["subscriptions"]
    friend_sub = [i for i in user_data["friends"][0]["watched"] and \
        user_data["friends"][1]["watched"] for k,v in i.items() if k=="host"]
    rec_host = [i for i in friend_sub for v in i.values() if v in user_sub]
    return rec_host

def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    rec_movies = [movie for friend in user_data["friends"] for movie \
        in friend["watched"] if movie["genre"]== fav_genre]
    return rec_movies 

def get_rec_from_favorites(user_data):
    rec_fav_movies = [movie for movie in user_data["favorites"] if movie not in \
        (i for friend in user_data["friends"] for i in friend["watched"])]
    return rec_fav_movies