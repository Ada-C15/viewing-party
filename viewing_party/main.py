def create_movie(movie_title, genre, rating):

    movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }
    for info in movie:
        if movie[info] == None:
            return None

    return movie

def add_to_watched(user_data, movie):

  user_data.update({"watched": [movie]})
  return user_data

def add_to_watchlist(user_data, movie):

  user_data.update({"watchlist":[movie]})
  return user_data  

def watch_movie(user_data, movie):

    for title in user_data["watchlist"]:
        if title["title"] == movie:
            user_data["watched"].append(title)
            user_data["watchlist"].remove(title)

    return user_data

def get_watched_avg_rating(user_data):

    ratings = []
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    
    return sum(ratings)/len(ratings)

def get_most_watched_genre(user_data):

    genres = []
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
      for genre in movie["genre"]:
        genres.append(movie["genre"])
        
    return max(set(genres), key=genres.count)

def get_friends_movies(user_data):

    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)

    return friends_movies

def get_unique_watched(user_data):
    
    unique_movies = []
    friends_movies = get_friends_movies(user_data)
    for movie in user_data["watched"]:
        if movie not in friends_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):

    user_movies = []
    friends_unique_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie)
    for movie in get_friends_movies(user_data):
        if movie not in user_movies:
            if movie not in friends_unique_movies:
                friends_unique_movies.append(movie)

    return friends_unique_movies

def get_available_recs(user_data):

    recommendations = []
    user_services = []
    for service in user_data["subscriptions"]:
        user_services.append(service)
    for movie in get_friends_movies(user_data):
        if movie["host"] in user_services:
            if movie not in recommendations:
                recommendations.append(movie)

    return recommendations

def get_new_rec_by_genre(user_data):

    rec_by_genre = []
    most_watched = get_most_watched_genre(user_data)
    for movie in get_friends_movies(user_data):
        if movie["genre"] == most_watched:
            rec_by_genre.append(movie)

    return rec_by_genre

def get_rec_from_favorites(user_data):
    user_favorites =user_data["favorites"]
    friends_watched = get_friends_movies(user_data)
    rec = []
    for item in user_favorites:
        if item not in friends_watched:
            rec.append(item)

    return rec

