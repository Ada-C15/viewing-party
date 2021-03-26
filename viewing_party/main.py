# Wave 1
def create_movie(title, genre, rating):
    # if bool(title) == True and bool(genre) == True and bool(rating) == True:
    if title and genre and rating:
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched": []
    }
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": []
    }
    user_data["watchlist"].append(movie)
    return user_data

'''
If title is in a movie in the user's watchlist, remove that movie
from watchlist and add that to watched.
'''
def watch_movie(user_data, title):

    user_data_copy = user_data.copy()

    for movie in user_data_copy["watchlist"]: # initial length: 2
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
            # break #Do I always need a break in a for-else loop? Or return will stop?
                # else:
                #     return user_data
            # return use_data
        # return use_data
    else:
        return user_data

# Wave 2
def get_watched_avg_rating(user_data):

    # for v in user_data.values():
    #     if v == []:
    #         return 0.0
    #     else:
    #         for movie in v:
    #             total_rating += movie["rating"]
    #         avg = total_rating / len(v)
    #         return avg

    if user_data["watched"] == []:
        return 0.0

    total_rating = 0
    for movie in user_data["watched"]:
            total_rating += movie["rating"]
            avg = total_rating / len(user_data["watched"])
    return avg

def get_most_watched_genre(user_data):
    genre_map = {}
    for movie in user_data["watched"]:
        x = movie["genre"]
        if x not in genre_map:
            genre_map[x] = 1
        else:
            genre_map[x] += 1
    
    most_watched_genre = (max(genre_map, key=genre_map.get)) if genre_map else None

    return most_watched_genre 

    # current_max = 0
    # for k, v in genre_map.items():
    #     if v > current_max:
    #         current_max = v
    
    # for k, v in genre_map.items():
    #     if v == current_max:
    #         return k

# Wave 3
'''
Determine which movies the user has watched, 
but none of their friends have watched.
'''
def get_unique_watched(user_data):

    mine_watched = {}
    for movie in user_data["watched"]:
        mine_watched[movie["title"]] = True
    
    friends_watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched[movie["title"]] = True

    diff = []
    for title in mine_watched.keys():
        if title not in friends_watched:
            diff.append({"title": title})
    return diff

    # movie_map = {}
    # for k,v in user_data.items():
    #     if k == "watched":
    #         for movie in v:
    #             x = movie["title"]
    #             if x not in movie_map:
    #                 movie_map[x] = 0  
    #     if k == "friends":
    #         for friend in v:
    #             for v in friend.values():
    #                 for title in v:
    #                     y = title["title"]
    #                     if y in movie_map:
    #                         movie_map[y] += 1

    # # Return a list of dictionaries, that represents a list of movies
    # holder = []
    # for k,v in movie_map.items():
    #     if v == 0:
    #         holder.append(k)

    # result = [{"title": i} for i in holder]

    # return result

'''
Determine which movies at least one of the user's friends have watched, 
but the user has not watched.
'''
def get_friends_unique_watched(user_data):

    mine_watched = {}
    for movie in user_data["watched"]:
        mine_watched[movie["title"]] = True
    
    friends_watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched[movie["title"]] = True

    diff = []
    for title in friends_watched.keys():
        if title not in mine_watched:
            diff.append({"title": title})
    return diff  

# Wave 4
'''
Determine a list of recommended movies. Add to list if:
The user has not watched it
At least one of the user's friends has watched
The "host" of the movie is a service that is in the user's "subscriptions"
'''
def get_available_recs(user_data):

    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    
    result = []
    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            result.append(movie)
    # [{'title': 'Title A', 'host': 'Service A'}, {'title': 'Title A', 'host': 'Service A'}, {'title': 'Title B', 'host': 'Service B'}]
    
    # Remove duplicates in rec_list
    rec_list = [i for n, i in enumerate(result) if i not in result[n + 1:]]
    return rec_list

# Wave 5
'''
Determine a list of recommended movies. Add to the list if:
The user has not watched it
At least one of the user's friends has watched
The "genre" of the movie is the same as the user's most frequent genre
'''
def get_new_rec_by_genre(user_data):

    # No recommendation if user watched list is empty
    if user_data["watched"] == []:
        return []

    # Get user's most frequently watched genre
    user_genre = []
    for movie in user_data["watched"]:
        user_genre.append(movie["genre"])
    most_watched_genre = (max(set(user_genre), key = user_genre.count))

    # Get movies that user hasn't watched but one of the user's friends has watched
    rec_movie = get_friends_unique_watched(user_data)
    # [{'title': 'Title D'}, {'title': 'Title E'}]

    # Find list of recommended movies
    result= []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if {"title": movie["title"]} in rec_movie and movie["genre"] == most_watched_genre:
                result.append(movie)
    return result

'''
Determine a list of recommended movies. Add to the list if:
The movie is in the user's "favorites"
None of the user's friends have watched it
'''
def get_rec_from_favorites(user_data):

    mine_watched = {}
    for movie in user_data["favorites"]:
        mine_watched[movie["title"]] = True
    
    friends_watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched[movie["title"]] = True

    result = []
    for title in mine_watched.keys():
        if title not in friends_watched:
            result.append({"title": title})
    return result




