# Nandita Gilroy's Viewing Party Project!
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
    genres = {}
    popular_genre = None
    counter = 0
    for movie in user_data["watched"]:
        current_genre = movie["genre"]
        if current_genre not in genres:
            genres[current_genre] = 1
        else:
            genres[current_genre] += 1

    for genre, occurances in genres.items():
        if occurances > counter:
            counter = occurances
            popular_genre = genre
    return popular_genre

def get_unique_watched(user_data):
    unique_movies = []
    for movie in user_data["watched"]:
        movie_is_unique = True
        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                movie_is_unique = False
        if movie_is_unique:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies 

def get_available_recs(user_data):
    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # If they have the movie subscription and it hasn't been added yet, 
            # add movie to recommendations
            if movie["host"] in user_data["subscriptions"] and movie not in recommendations:
                recommendations.append(movie)
    return recommendations

def get_new_rec_by_genre(user_data):
    recommendations = []
    favorite_genre = get_most_watched_genre(user_data)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == favorite_genre and movie not in recommendations:
                recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    for movie in user_data["favorites"]:
        recommend_movie = True
        for friend in user_data["friends"]:
            if movie in friend["watched"] or movie in recommendations:
                recommend_movie = False
        if recommend_movie:
                recommendations.append(movie)
    return recommendations