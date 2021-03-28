def create_movie(movie_title, genre, rating):
    if movie_title == None:
        return None
    elif genre == None:
        return None
    elif rating == None:
        return None
    else:
        movie = {"title": movie_title,
                "genre": genre,
                "rating": rating}
        return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie_title):
    # print("****** before execution *****")
    # print(user_data)
    watchlist = user_data["watchlist"]
    for i in range(len(watchlist)):
        if watchlist[i]["title"] == movie_title:
            movie = watchlist[i]
            add_to_watched(user_data, movie)
            #remove from watchlist
            watchlist.remove(movie)
            return user_data
    else:
        return user_data

def get_watched_avg_rating(user_data):
    watchedlist = user_data["watched"]
    ratings = []
    if len(watchedlist) == 0:
        return 0.0
    else:
        for i in range(len(watchedlist)):
            ratings.append(watchedlist[i]["rating"])
        ratings_sum = 0
        for i in ratings:
            ratings_sum = ratings_sum + i
        average = ratings_sum/len(ratings)
        print(average)
        return average

def get_most_watched_genre(user_data):
    genres = {}
    watchedlist = user_data["watched"]
    if len(watchedlist) == 0:
        return None
    else:
        for i in range(len(watchedlist)):
            if watchedlist[i]["genre"] not in genres:
                genres[watchedlist[i]["genre"]] = 1
            else:
                genres[watchedlist[i]["genre"]] += 1
    sort_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)
    return sort_genres[0][0]

def get_unique_watched(user_data):
    userwatched = user_data["watched"]
    friendswatched = user_data["friends"]
    unique_watched = []
    friendtitlelist = []
    for friend in friendswatched:
        watched = friend["watched"]
        for title in watched:
            friendtitlelist.append(title["title"])
    for title in userwatched:
        if title["title"] not in friendtitlelist:
            unique_watched.append(title)
    return unique_watched

def get_friends_unique_watched(user_data):
    userwatched = user_data["watched"]
    friendswatched = user_data["friends"]
    userlist = []
    unique_watched = []
    for title in userwatched:
        userlist.append(title["title"])
    for friend in friendswatched:
        watched = friend["watched"]
        for title in watched:
            if title["title"] not in userlist:
                if title not in unique_watched:
                    unique_watched.append(title)
    print(unique_watched)
    return unique_watched


def get_available_recs(user_data):
    user_hosts_list = user_data["subscriptions"]
    user_watched_list = user_data["watched"]
    friends_dictkey_watched_list_of_dicts = user_data["friends"]
    users_list_of_watched_titles = []
    recommendations = []
    for title in user_watched_list:
        users_list_of_watched_titles.append(title["title"])
    for friend in friends_dictkey_watched_list_of_dicts:
        friends_watched_list_of_dicts = friend["watched"]
        for movie in friends_watched_list_of_dicts:
            if movie["title"] not in users_list_of_watched_titles:
                if movie["host"] in user_hosts_list:
                    if movie not in recommendations:
                        recommendations.append(movie)
    
    return recommendations 


def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    user_watched_list = user_data["watched"]
    friends_dictkey_watched_list_of_dicts = user_data["friends"]
    users_list_of_watched_titles = []
    recommendations = []
    for title in user_watched_list:
        users_list_of_watched_titles.append(title["title"])
    for friend in friends_dictkey_watched_list_of_dicts:
        friends_watched_list_of_dicts = friend["watched"]
        for movie in friends_watched_list_of_dicts:
            if movie["title"] not in users_list_of_watched_titles:
                if movie["genre"] is most_watched_genre:
                    if movie not in recommendations:
                        recommendations.append(movie)
    print(recommendations)
    return recommendations 

def get_rec_from_favorites(user_data):
    #creating variables for easier access to nested data
    user_fave_dictkey_list_of_dicts = user_data["favorites"]
    friends_dictkey_watched_list_of_dicts = user_data["friends"]
    friends_list_of_watched_titles = []
    recommendations = []

    #putting titles into list for easier sorting/comparison.
    for friend in friends_dictkey_watched_list_of_dicts:
        friends_watched_list_of_dicts = friend["watched"]
        for movie in friends_watched_list_of_dicts:
            friends_list_of_watched_titles.append(movie["title"])
    #comparing movies in user favorites to friends watched movies
    for movie in user_fave_dictkey_list_of_dicts:
        #checking if movies in users faves are not in friends watched 
        if movie["title"] not in friends_list_of_watched_titles:
            recommendations.append(movie)
    print(recommendations)
    return recommendations