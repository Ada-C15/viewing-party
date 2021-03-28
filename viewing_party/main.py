
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

    genre_count = []
    genre_stats = dict()
    most_watched_genre = ""

    if not user_data["watched"]:
        return None 
    for keys, values in user_data.items():
        for watched_movies in values:
            genre_count.append(watched_movies['genre'])
    

    for value in genre_count:
        if value not in genre_stats:
            genre_stats[value] = 1
        else:
            genre_stats[value] +=1

    most_watched_genre_tuple = [(value, key) for key, value in genre_stats.items()]
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
    user_watched = []
    user_subs = []
    temp = []
    recommendations_list = []

    for item in user_data["watched"]:
        if user_data["watched"]:
            user_watched.append(item)

    for item in user_data["subscriptions"]:
        if user_data["subscriptions"]:
            user_subs.append(item)

    for item in user_data["friends"]:
        for k,v in item.items():
            for item in v:
                if item["title"] not in user_watched and item["host"] in user_subs:
                    temp.append(item)
    
    for i in range(len(temp)):
        if temp[i] not in temp[i + 1:]:
            recommendations_list.append(temp[i])
    
    return recommendations_list

def get_new_rec_by_genre(user_data):
    count_list = []
    genre_stats = dict()
    most_watched_genre = ""
    recommendations_by_genre = []

    if not user_data["watched"]:
        return recommendations_by_genre

    for item in user_data["watched"]:
        count_list.append(item["genre"])
    
    
    for value in count_list:
        if value not in genre_stats:
            genre_stats[value] = 1
        else:
            genre_stats[value] += 1
    
    temp = [(value, key) for key, value in genre_stats.items()]
    most_watched_genre = max(temp)[1]

    for item in user_data["friends"]:
        for k,v in item.items():
            for item in v:
                if item["title"] not in user_data["watched"] and item["genre"] == most_watched_genre:
                    recommendations_by_genre.append(item)
    
    return recommendations_by_genre


def get_rec_from_favorites(user_data):
    users_favorites = []
    friends_watched = []
    temp = []
    recommendations_by_favorites = []

    for item in user_data["favorites"]:
        users_favorites.append(item)
    
    for item in user_data["friends"]:
        for key,value in item.items():
            for item in value:
                for k,v in item.items():
                    friends_watched.append(v)
    
    for item in user_data["watched"]:
        for key,value in item.items():
            if value not in friends_watched:
                temp.append(item)
    
    for item in temp:
        if item in users_favorites:
            recommendations_by_favorites.append(item)
    
    return recommendations_by_favorites

    








    


