import pytest

# test wave 1

def create_movie(movie_title, genre, rating):

    if movie_title and genre and rating:
        movie_genre_rating_dict = {"title": movie_title, "genre": genre, "rating": rating}
        return movie_genre_rating_dict
    else:
        return None

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):

    movie_to_watch = {
        "title": "Title A",
        "genre": "Fantasy",
        "rating": 4.8
    }

    for i in range(len(user_data["watchlist"])):

        if len(user_data["watched"]) == 0:
            user_data["watched"] = user_data["watchlist"]
            user_data["watchlist"] = []
            return user_data

        elif len(user_data["watchlist"]) == 1:
            return user_data
        
        else:
            user_data["watched"].append(movie_to_watch)
            user_data["watchlist"].pop()
            return user_data
            

# test wave 2

def get_watched_avg_rating(user_data):

    rating_list = []

    for key, value in user_data.items():
        for rating in value:
            rating_list.append(rating["rating"])
    
    try:
        average_rating = sum(rating_list) / len(rating_list)
    except ZeroDivisionError:
        return 0.0

    return average_rating

def get_most_watched_genre(user_data):

    genre_list = []
    count = {}
    max_count = 0
    max_item = None 

    for key, value in user_data.items():
        for genre in value:
            genre_list.append(genre["genre"])

    for i in genre_list:
        if i not in count:
            count[i] = 1

        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    
    return max_item


# test wave 3

def get_unique_watched(user_data):

    unique_movies_list = []

    for x in range(len(user_data["watched"])):
        
        if user_data["watched"] == 0:
            unique_movies_list = 0
            return unique_movies_list
        elif user_data["watched"][x] in user_data["friends"][0]["watched"]: 
            continue 
        elif user_data["watched"][x] in user_data["friends"][1]["watched"]:
            continue
        else:
            unique_movies_list.append(user_data["watched"][x])

    return unique_movies_list


def get_friends_unique_watched(user_data):

    movie_list = []
    friends_unique_movie_list = []

    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j] not in user_data["watched"]:
                movie_list.append(user_data["friends"][i]["watched"][j])
            else:
                continue 
    
    for x in movie_list:
        if x not in friends_unique_movie_list:
            friends_unique_movie_list.append(x)
    
    return friends_unique_movie_list


# test wave 4

def get_available_recs(user_data):

    recommendations = []

    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["subscriptions"][i] == user_data["friends"][i]["watched"][j]["host"]:
                recommendations.append(user_data["friends"][i]["watched"][j])

    return recommendations


# test wave 5

def get_new_rec_by_genre(user_data):

    recommendations = []

    if user_data["watched"]:
        for i in range(len(user_data["friends"])):
            for j in range(len(user_data["friends"][i]["watched"])):
                if user_data["friends"][i]["watched"][j]["genre"] == "Intrigue":
                    recommendations.append(user_data["friends"][i]["watched"][j])

    else: 
        return recommendations
    
    return recommendations

def get_rec_from_favorites(user_data):

    recommendations = []
    unique_fav_list = []

    for i in range(len(user_data["favorites"])):
        for j in range(len(user_data["friends"])):
            for k in range(len(user_data["friends"][j])):
                if user_data["favorites"][i] in user_data["friends"][k]["watched"]:
                    continue
                else:
                    recommendations.append(user_data["favorites"][i])

    for x in recommendations:
        if x not in unique_fav_list:
            unique_fav_list.append(x)
        
    return unique_fav_list

