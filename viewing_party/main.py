# Viewing Party Project!
def create_movie(movie_title, genre, rating):
    new_movie = {}
    if movie_title and genre and rating:
        new_movie["title"] = movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    if user_data["watched"]:
        sum_rating = 0
        for movie in user_data["watched"]:
            sum_rating += movie["rating"]
        watched_avg_rating = sum_rating/len(user_data["watched"])
    else:
        watched_avg_rating = 0
    return watched_avg_rating

def get_most_watched_genre(user_data):
    #go through genres and add them to list
    #go through and add list of genres to dict?
    #use .get with dicts
    genres = {
        "Fantasy": 0,
        "Horror": 0,
        "Intrigue": 0,
    }
    popular_genre = None
    counter = 0
    for movie in user_data["watched"]:
        genres[movie["genre"]] += 1

    for genre, occurances in genres.items():
        if occurances > counter:
            counter = occurances
            popular_genre = genre
        else:
            continue
    return popular_genre

def get_unique_watched(user_data):
    unique_movies = []
    for movie in user_data["watched"]:
        movie_is_unique = True
        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                movie_is_unique = False
            else:
                continue
        if movie_is_unique:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in user_data["watched"]:
                continue
            elif movie in friends_unique_movies:
                continue
            else:
                friends_unique_movies.append(movie)
    return friends_unique_movies 

def get_available_recs(user_data):
    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # If they have the movie subscription and it hasn't been added yet, add movie to recommendations
            if movie["host"] not in user_data["subscriptions"]:
                continue
            elif movie in recommendations:
                continue
            else:
                recommendations.append(movie)
    return recommendations

def get_new_rec_by_genre(user_data):
    recommendations = []
    favorite_genre = get_most_watched_genre(user_data)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] != favorite_genre:
                continue
            elif movie in recommendations:
                continue
            else:
                recommendations.append(movie)
    return recommendations

#I think the 2nd to last test_wave_05 test is testing the wrong function
def get_rec_from_favorites(user_data):
    recommendations = []
    for movie in user_data["favorites"]:
        recommend_movie = True
        for friend in user_data["friends"]:
            if movie in friend["watched"] or movie in recommendations:
                recommend_movie = False
            else:
                continue
        if recommend_movie:
                recommendations.append(movie)
    return recommendations

#Now what? Do I need to put all these functions together?

