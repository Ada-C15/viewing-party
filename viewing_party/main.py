def create_movie(title, genre, rating):
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
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

def watch_movie(user_data, title):

    for k,v in user_data.items():
        # k: watchlist, v: [...] (2)
        # k: watched, v: [...] (1)
        if k == "watchlist":
            for movie in v: # initial length: 2
                if movie["title"] == title:
                    user_data["watchlist"].remove(movie)
                    user_data["watched"].append(movie)
                    return user_data
                # else:
                #     return user_data
            # return use_data
        # return use_data
    return user_data

def get_watched_avg_rating(user_data):
    total_rating = 0
    for v in user_data.values():
        if v == []:
            return 0.0
        else:
            for movie in v:
                total_rating += movie["rating"]
            avg = total_rating / len(v)
            return avg

def get_most_watched_genre(user_data):
    genre_map = {}
    for v in user_data.values():
        for movie in v:
            x = movie["genre"]
            if x not in genre_map:
                genre_map[x] = 1
            else:
                genre_map[x] += 1
    
    current_max = 0
    for k, v in genre_map.items():
        if v > current_max:
            current_max = v
    
    for k, v in genre_map.items():
        if v == current_max:
            return k

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
    return (diff)

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
    return (diff)     

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
    rec_list = [i for n, i in enumerate(result) if i not in result[n + 1:]]
    return rec_list






