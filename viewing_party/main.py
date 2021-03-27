
def create_movie(title, genre, rating): 
    movie = dict();
    if title:
        movie['title'] = title;
    else:
        return None
    if genre:
        movie['genre'] = genre;
    else:
        return None
    if rating:
        movie['rating'] = rating;
    else:
        return None
    return movie


def add_to_watched(user_data, movie):   
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    watched_movie_temp_list = []

    for key, values in user_data.items():
        for movie_info in values:
            if title == movie_info["title"]:
                user_data["watchlist"].remove(movie_info)
                watched_movie_temp_list.append(movie_info)
    for watched_movie in watched_movie_temp_list:
        user_data["watched"].append(watched_movie)

    return user_data


def get_watched_avg_rating(user_data):

    average_ratings = []
    average = []

    if not user_data["watched"]:
        return 0.0

    for keys, values in user_data.items():
        for watched_movies in values:   
            if watched_movies["rating"] == '':
                watched_movies["rating"] = 0.0
            else:
                average_ratings.append(float(watched_movies["rating"]))
                average = sum(average_ratings)/len(average_ratings)
        return average

def get_most_watched_genre(user_data):

    genre_count_list = []
    genre_stats_dict = dict()
    most_watched_genre = ""

    if not user_data["watched"]:
        return None 
    for keys, values in user_data.items():
        for watched_movies in values:
            genre_count_list.append(watched_movies['genre'])
    

    for value in genre_count_list:
        if value not in genre_stats_dict:
            genre_stats_dict[value] = 1
        else:
            genre_stats_dict[value] +=1
    print(genre_stats_dict)

    most_watched_genre_tuple = [(value, key) for key, value in genre_stats_dict.items()]
    most_watched_genre = max(most_watched_genre_tuple)[1]
    return most_watched_genre


def get_unique_watched(user_data):
    user_watched = []
    friends_watched = []
    movies_unique_to_friends_list = []
    

    for element in user_data["friends"]:
        for k,v in element.items():
            for item in v:
                for k,v in item.items():
                    friends_watched.append(v)
    
    for element in user_data["watched"]:
        for k,v in element.items():
            user_watched.append(v)
            if v not in friends_watched:
                movies_unique_to_friends_list.append(element)  
    return movies_unique_to_friends_list

def get_friends_unique_watched(user_data):
    user_watched = []
    friends_watched = []
    temp = []
    movies_unique_to_user_list = []

    for element in user_data["watched"]:
        for k,v in element.items():
            user_watched.append(v)

    for element in user_data["friends"]:
        for k,v in element.items():
            for item in v:
                for k,v in item.items():
                    if v not in user_watched:
                        temp.append(item)

    for i in range(len(temp)):
        if temp[i] not in temp[i+1:]:
            movies_unique_to_user_list.append(temp[i])
            
    return movies_unique_to_user_list


def get_available_recs(user_data):
    pass








    


