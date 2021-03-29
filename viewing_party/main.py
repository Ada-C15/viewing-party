#Test Wave 1
def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        return {
            "title": movie_title,
            "genre": genre, 
            "rating": rating
            }


def add_to_watched(user_data, movie):
    # user_data = {
    #     "watched": [{
    #         "title": "Title A",
    #         "genre": "Horror",
    #         "rating": 3.5
    # }]
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data


# Test Wave 2
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    for movie in user_data["watched"]:
        avg_rating = (movie["rating"])/len(user_data["watched"]) + avg_rating
    return avg_rating


def calculate_genre_freq(watched):
    genre_freq_dict = {}
    # print(user_data)
    # print(user_data["watched"])
    # watch_list = user_data["watched"]
    # watch_list = user_data["watched"]
    for movie in watched:
        genre = movie["genre"]
        if genre in genre_freq_dict.keys():
            genre_freq_dict[genre] += 1
        else: 
            genre_freq_dict[genre] = 1
        
    return genre_freq_dict


def get_most_watched_genre(user_data):
    # how would you call the helper function here ?
    # print(user_data)
    # print(user_data["watched"])

    watched = user_data["watched"]
    genre_freq_dict = calculate_genre_freq(watched)
    most_popular = 0
    most_popular_genre = ""
    # print("before the loop")
    # what if there was an empty list
    if len(watched) == 0:
        return None
    for key,value in genre_freq_dict.items():
        if value > most_popular:
            most_popular = value
            most_popular_genre = key
    # print("after the loop")

    return most_popular_genre


# Test Wave 3
def get_unique_watched(user_data):
    friends_list = []
    for friends_movie in user_data["friends"]:
        for friends_watched in friends_movie["watched"]:
            friends_list.append(friends_watched)
    
    unique_watched_list = []
    for unique_movie in user_data["watched"]:
        if unique_movie not in friends_list:
            unique_watched_list.append(unique_movie)
    
    return unique_watched_list


def get_friends_unique_watched(user_data): 
    unique_movie = []
    for friends_watched in user_data["friends"]:
        for movie in friends_watched["watched"]:
            if movie not in user_data["watched"] and movie not in unique_movie:
                unique_movie.append(movie)
    
    return unique_movie



# Test Wave 4
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommend_movies = []
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommend_movies.append(movie)
    
    return recommend_movies


# Test Wave 5
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    print(most_watched_genre)
    new_genre_recs = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_watched_genre and movie not in user_data["watched"]:
                new_genre_recs.append(movie)
    
    return new_genre_recs
"""
    look at most watched genre in user's list
    look at user's friend's list of movies they've 
    watched in same genre that user most watched, but hasn't watched yet
    recommend list of movies from that genre user hasn't watched 
"""


def get_rec_from_favorites(user_data):
    fav_recs = []
    all_friends_watched = []
    for friend in user_data["friends"]:
        all_friends_watched += friend["watched"]
    for movie in user_data["favorites"]:
        if movie not in all_friends_watched:
            fav_recs.append(movie)

    return fav_recs

