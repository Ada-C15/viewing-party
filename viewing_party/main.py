from collections import defaultdict


def create_movie(movie_title, genre, rating):
    user_data = {}
    if movie_title and genre and rating:
        user_data["title"] = movie_title
        user_data["genre"] = genre
        user_data["rating"] = rating
        return user_data

    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:  
            new_title = user_data["watchlist"][i]

            user_data["watched"].append(new_title)
            user_data["watchlist"].remove(new_title)
    return user_data

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    sum = 0.0
    count = 0
    for i in range(len(user_data["watched"])):
        sum = sum + user_data["watched"][i]["rating"]
        count = count + 1
    if sum > 0 and count > 0:
        avg_rating = sum / count
    return avg_rating

def get_most_watched_genre(user_data):
    genre = defaultdict(int)
    for i in range(len(user_data["watched"])):
        genre_for_movie = user_data["watched"][i]["genre"]
        genre[genre_for_movie] += 1

    frequency = 0
    most_popular_genre = None
    for j, v in genre.items():
        if v > frequency:
            frequency = v
            most_popular_genre = j
    return most_popular_genre    

def get_unique_watched(user_data):
    user_watched_dic_list = []
    friends_watched_dic_list = []
    users_unique_movies = []

    # create list of user movies:
    for i in range(len(user_data["watched"])):
        user_watched_dic = user_data["watched"][i]
        user_watched_dic_copy = user_watched_dic.copy()
        user_watched_dic_list.append(user_watched_dic_copy)

    # create list of friends movies
    for j in range(len(user_data["friends"])):
        for k in range(len(user_data["friends"][j]["watched"])):
            friends_watched_dic = user_data["friends"][j]["watched"][k]
            friends_watched_dic_copy = friends_watched_dic.copy() 
            if friends_watched_dic_copy not in friends_watched_dic_list:
                friends_watched_dic_list.append(friends_watched_dic_copy)   

    #reate list of unique movies:
    for i in range(len(user_watched_dic_list)):
        if user_watched_dic_list[i] not in friends_watched_dic_list:
               movie = user_watched_dic_list[i]
               movie_copy = movie.copy()
               users_unique_movies.append(movie_copy)

    return users_unique_movies

def get_friends_unique_watched(user_data):
    user_watched_dic_list = []
    friends_watched_dic_list = []
    friends_unique_movies = []

    # create list of user movies:
    for i in range(len(user_data["watched"])):
        user_watched_dic = user_data["watched"][i]
        user_watched_dic_copy = user_watched_dic.copy()
        user_watched_dic_list.append(user_watched_dic_copy)

    # create list of friends movies
    for j in range(len(user_data["friends"])):
        for k in range(len(user_data["friends"][j]["watched"])):
            friends_watched_dic = user_data["friends"][j]["watched"][k]
            friends_watched_dic_copy = friends_watched_dic.copy() 
            if friends_watched_dic_copy not in friends_watched_dic_list:
                friends_watched_dic_list.append(friends_watched_dic_copy)   

    #reate list of unique movies:
    for i in range(len(friends_watched_dic_list)):
        if friends_watched_dic_list[i] not in user_watched_dic_list:
               movie = friends_watched_dic_list[i]
               movie_copy = movie.copy()
               friends_unique_movies.append(movie_copy)

    return friends_unique_movies
        
def get_available_recs(user_data):
    friends_movies_l = []
    user_movies_l = []
    recommended_l = []

    for i in range(len(user_data["watched"])):
        user_watched_dic = user_data["watched"][i]
        user_watched_dic_copy = user_watched_dic.copy()
        user_movies_l .append(user_watched_dic_copy)

    for j in range(len(user_data["friends"])):
        for k in range(len(user_data["friends"][j]["watched"])):
            friends_watched_dic = user_data["friends"][j]["watched"][k]
            friends_watched_dic_copy = friends_watched_dic.copy() 
            if friends_watched_dic_copy not in friends_movies_l:
                friends_movies_l.append(friends_watched_dic_copy)   

    for k in range(len(friends_movies_l)):
        if friends_movies_l[k] not in user_movies_l and friends_movies_l[k]["host"] in user_data["subscriptions"]:
            friends_movie = friends_movies_l[k]
            friends_movie_copy = friends_movie.copy()
            recommended_l.append(friends_movie_copy)

    return recommended_l
   
def get_new_rec_by_genre(user_data):
    frequency = ""
    recommendations = []
    friends_movies_l = []
    user_movies_l = []

    genre_dic_freq = defaultdict(int)

    #make list of friends movies
    for i in range(len(user_data["watched"])):
        user_watched_dic = user_data["watched"][i]
        user_watched_dic_copy = user_watched_dic.copy()
        user_movies_l .append(user_watched_dic_copy)

    #make list of user movies
    for j in range(len(user_data["friends"])):
        for k in range(len(user_data["friends"][j]["watched"])):
            friends_watched_dic = user_data["friends"][j]["watched"][k]
            friends_watched_dic_copy = friends_watched_dic.copy() 
            if friends_watched_dic_copy not in friends_movies_l:
                friends_movies_l.append(friends_watched_dic_copy)   
    
    #   count the "genre" frequency
    for m in range(len(user_data["watched"])):
        watched_genre = user_data["watched"][m]["genre"]
        genre_dic_freq[watched_genre] += 1
    start_val = 0
    for key, value in genre_dic_freq.items():
        if value > start_val:
            start_val = value
            frequency = key

    # for i range(len(friends movies)):
    for n in range(len(friends_movies_l)):
            if (friends_movies_l[n] not in user_movies_l) and (friends_movies_l[n]["genre"] == frequency):
                movie = (friends_movies_l[n]).copy()
                recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    friends_movies_l = []
    user_favs_l = []

    for i in range(len(user_data["favorites"])):
        user_watched_dic = user_data["favorites"][i]
        user_watched_dic_copy = user_watched_dic.copy()
        user_favs_l .append(user_watched_dic_copy)

    for j in range(len(user_data["friends"])):
        for k in range(len(user_data["friends"][j]["watched"])):
            friends_watched_dic = user_data["friends"][j]["watched"][k]
            friends_watched_dic_copy = friends_watched_dic.copy() 
            if friends_watched_dic_copy not in friends_movies_l:
                friends_movies_l.append(friends_watched_dic_copy) 
    
    for m in range(len(user_favs_l)):
        if user_favs_l[m] not in friends_movies_l:
            recom_movie = user_favs_l[m]
            recom_movie_copy = recom_movie.copy()
            recommendations.append(user_favs_l[m])
    print(recommendations)
    return recommendations
