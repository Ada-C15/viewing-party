def create_movie(title,genre,rating):
    new_movie = {
        "title": "",
        "genre": "",
        "rating": 0
    }
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None


def add_to_watched(user_data,movie):
    for key, value in user_data.items():
        user_data[key].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    for key, value in user_data.items():
        user_data[key].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movies in user_data["watchlist"]:
        if title == movies["title"]:
            user_data["watched"].append(movies)
            user_data["watchlist"].pop(0)
    return user_data

def get_watched_avg_rating(user_data):
    rating_list = []
    if user_data["watched"]:
        for movies in user_data["watched"]:
            rating_list.append(movies["rating"])
        return sum(rating_list)/len(rating_list)
    else:
        return 0.0

def get_most_watched_genre(user_data):
    word_counter = {}
    genre_list = []
    if user_data["watched"]:
        for movies in user_data["watched"]:
            genre_list.append(movies["genre"])
        for genres in genre_list:
            if genres in word_counter:
                word_counter[genres] += 1
            else:
                word_counter[genres] = 1
        most_watched = sorted(word_counter, key = word_counter.get, reverse = True)
        return most_watched[0]
    else:
        return None

#get_friends_movie_list() is a helper function that iterates through the user_data's friend movie list
def get_friends_movie_list(user_data):
    friends_movie_list = []
    for friends_watched_movies in user_data["friends"]:
        for watched, movies in friends_watched_movies.items():
            friends_movie_list.append(movies)
    comprehensive_friend_list = (friends_movie_list[0] + friends_movie_list[1])
    return comprehensive_friend_list

def get_unique_watched(user_data):
    friends_list = get_friends_movie_list(user_data)
    my_movie_list = []
    unique_movies = []
    for my_watched_movies in user_data["watched"]:
        my_movie_list.append(my_watched_movies)
    for items in my_movie_list:
        if items not in friends_list:
            unique_movies.append(items)
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_list = get_friends_movie_list(user_data)
    my_movie_list = []
    unique_movies = []
    shared_movies = []
    for my_watched_movies in user_data["watched"]:
        my_movie_list.append(my_watched_movies)
    for items in friends_list:
        if items not in my_movie_list:
            shared_movies.append(items)
    for movie_items in shared_movies:
        if movie_items not in unique_movies:
            unique_movies.append(movie_items)
    return unique_movies

def get_available_recs(user_data):
    friends_list = get_friends_movie_list(user_data)
    recommended_movies = []
    new_movies = []
    new_recommended = []
    for movies_and_hosts in friends_list:
        if movies_and_hosts not in user_data["watched"]:
            new_movies.append(movies_and_hosts)
    for recommended in new_movies:
        if recommended["host"] in user_data["subscriptions"]:
            recommended_movies.append(recommended)
    for delete_duplicates in recommended_movies:
        if delete_duplicates not in new_recommended:
            new_recommended.append(delete_duplicates)
    return new_recommended

#get_friends_movie_titles() is ahelper function that creates a list of friend's
#titles in user_data
def get_friends_movie_titles(user_data):
    friends_titles = []
    for friends_watched_movies in user_data["friends"]:
        for friends_movie_titles in friends_watched_movies["watched"]:
            friends_titles.append(friends_movie_titles)
    return friends_titles

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    my_movies = []
    friends_movies = get_friends_movie_titles(user_data)
    favorite_genre = get_most_watched_genre(user_data)
    for my_watched_movies in user_data["watched"]:
        my_movies.append(my_watched_movies["title"])
    for movie_titles in friends_movies:
        if movie_titles["title"] not in my_movies and movie_titles["genre"] == favorite_genre:
            recommended_movies.append(movie_titles)
    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    my_friends_movies = get_friends_movie_titles(user_data)
    favorites = []
    for my_movies in user_data["favorites"]:
        favorites.append(my_movies)
    for movies in favorites:
        if movies not in my_friends_movies:
            recommended_movies.append(movies)
    return recommended_movies