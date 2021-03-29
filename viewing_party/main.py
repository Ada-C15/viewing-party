#Wave 1 

def create_movie(movie_title, genre, rating):
    new_movie = None
    if movie_title and genre and rating:
        new_movie = {
            "title":movie_title,        "genre": genre,
            "rating": rating 
        }
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"] 
    for movie in watchlist:
        for movie_info in movie.values():
            if movie_info == title:
                user_data["watched"].append(movie)
                watchlist.remove(movie)
    return user_data


#Wave 2

def get_watched_avg_rating(user_data):
    sum_rating = 0.0
    watched_list = user_data["watched"]
    for movie in watched_list:
        for movie_val in movie.values():
            if type(movie_val) == float:
                movie_rating =  movie_val
                sum_rating += movie_rating
    avg_rating = sum_rating/len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data): 
    watched_list = user_data["watched"]
    genre_dict = {}
    for movie in watched_list:
        for movie_info, info in movie.items():
            if movie_info == "genre":
                movie_genre = info
                if movie_genre not in genre_dict:
                    genre_dict[movie_genre] = 1
                else: 
                    genre_dict[movie_genre] += 1
    
    most_watched_genre = None
    max_found = None
    
    for genre, genre_frequency in genre_dict.items():
        if max_found is None or genre_frequency > max_found:
            max_found = genre_frequency
            most_watched_genre = genre
    return most_watched_genre

#Wave 3 

def get_unique_watched(user_data):
    u_unique_watched = {}
    user_titles = []
    friends_titles = []
    user_watched_list = user_data["watched"]
    for movie_dict in user_watched_list:
        for movie, movie_title in movie_dict.items():
            user_titles.append(movie_title)
    print(user_titles)


    friends_watched_lists = user_data["friends"]
    for friends_dict in friends_watched_lists:
        for title_dict in friends_dict["watched"]:
            f_title = title_dict["title"]
            friends_titles.append(f_title)
    print(friends_titles)
    
    u_unique_titles = find_user_diff(user_titles, friends_titles)
    u_unique_dict_list = []
    for u_title in u_unique_titles:
        u_unique_dict_list.append({"title":u_title})
    print(u_unique_dict_list)
    return u_unique_dict_list

def find_user_diff(unique_list, comp_list):
    differences = []
    for a in unique_list:
        if a not in differences:
            found = False
            for b in comp_list:
                if a == b:
                    found = True
            if not found:
                differences.append(a)
    return differences


def get_friends_unique_watched(user_data):
    u_unique_watched = {}
    user_titles = []
    friends_titles = []
    user_watched_list = user_data["watched"]
    for movie_dict in user_watched_list:
        for movie, movie_title in movie_dict.items():
            user_titles.append(movie_title)
    #print(user_titles)


    friends_watched_lists = user_data["friends"]
    for friends_dict in friends_watched_lists:
        for title_dict in friends_dict["watched"]:
            f_title = title_dict["title"]
            friends_titles.append(f_title)
    #print(friends_titles)
    
    f_unique_titles = find_user_diff(friends_titles, user_titles)
    f_unique_dict_list = []
    for f_title in f_unique_titles:
        f_unique_dict_list.append({"title":f_title})   
    print(f_unique_dict_list)
    return(f_unique_dict_list)

#Wave 4:

def get_available_recs(user_data):
    user_watched = user_data["watched"]
    user_subs_list = user_data["subscriptions"]
    friends_list = user_data["friends"]
    friend_recs = []
    
    for f_watched in friends_list:
        for friend_dict in f_watched["watched"]:
            host = friend_dict["host"]
            if host in user_subs_list and friend_dict not in friend_recs:
                friend_recs.append(friend_dict)
    return friend_recs

#Wave 5

def get_new_rec_by_genre(user_data):
    most_watched = get_most_watched_genre(user_data)
    print(most_watched)
    user_watched = user_data["watched"]
    friends_list = user_data["friends"]
    friend_recs = []

    for f_watched in friends_list:
        for friend_dict in f_watched["watched"]:
            genre = friend_dict["genre"]
            if genre == most_watched and friend_dict not in friend_recs:
                friend_recs.append(friend_dict)
    return friend_recs
    
def get_rec_from_favorites(user_data):
    user_favs = user_data["favorites"]
    friends_list = user_data["friends"]
    user_recs = []

    for u_fav_movie in user_favs:
        found = False
        for friend_dict in friends_list:
            f_watched = friend_dict["watched"]
            if (u_fav_movie in f_watched) or (u_fav_movie in user_recs):
                found = True
        if found == False:
            user_recs.append(u_fav_movie)
    return user_recs