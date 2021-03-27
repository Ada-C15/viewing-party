#WAVE 1 *******************************************************************************************************************************************************

def create_movie(title, genre, rating):
    while title and genre and rating:
        return {"title":title, "genre":genre, "rating":rating}
        
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for header in user_data["watchlist"]:
        if header["title"] == title:
            user_data["watchlist"].remove(header)
            user_data["watched"].append(header)
    return user_data


#WAVE 2 *******************************************************************************************************************************************************

def get_watched_avg_rating(user_data):
    total = 0
    if len(user_data["watched"]) == 0:
        return 0
    for movie in user_data["watched"]:
        total += movie["rating"]
    else:
        return total/len(user_data["watched"])

def get_most_watched_genre(user_data):
    all_genres = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in all_genres:
            all_genres[movie["genre"]] = 1
        else:
            all_genres[movie["genre"]] += 1
    if len(user_data["watched"]) == 0:
        return None
    most_watched = max(all_genres, key=all_genres.get)
    return most_watched

#WAVE 3 ******************************************************************************************************************************************************

def get_unique_watched(user_data):
    unseen_movies = []
    movies_seen_by_friends = []
    movies_seen_by_user = user_data["watched"]
    for friends_watched in user_data["friends"]:
        for friends_title in friends_watched["watched"]:
            movies_seen_by_friends.append(friends_title)

    for watched_title in movies_seen_by_user:
        if watched_title in movies_seen_by_friends:
            continue
        unseen_movies.append(watched_title)
            
    return unseen_movies

def get_friends_unique_watched(user_data):
    unseen_movies = []
    movies_seen_by_friends = []
    movies_seen_by_user = user_data["watched"]
    for friends_watched in user_data["friends"]:
        for friends_title in friends_watched["watched"]:
            movies_seen_by_friends.append(friends_title)

    for watched_title in movies_seen_by_friends:
        if watched_title not in unseen_movies:
            if watched_title in movies_seen_by_user:
                continue
            unseen_movies.append(watched_title)
    return unseen_movies



#WAVE 4 *******************************************************************************************************************************

def get_available_recs(user_data):
    list_of_movies = []
    yet_to_watch = get_friends_unique_watched(user_data)
    
    for available_movies in yet_to_watch:
        if available_movies["host"] in user_data["subscriptions"]:
            list_of_movies.append(available_movies)
    return list_of_movies


#WAVE 5 *********************************************************************************************************************************

def get_new_rec_by_genre(user_data):
    most_genre = get_most_watched_genre(user_data)
    rec_movies = get_friends_unique_watched(user_data)
    rec_genre = []
    
    for movie in rec_movies:
        if movie["genre"] == most_genre:
            rec_genre.append(movie)
    return rec_genre


def get_rec_from_favorites(user_data):
    seen_movies = get_unique_watched(user_data)
    rec_list = []

    for movies in seen_movies:
        if movies in user_data["favorites"]:
            rec_list.append(movies)
    return rec_list