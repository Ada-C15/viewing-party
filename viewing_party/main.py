def create_movie(movie_title, genre, rating):
    new_movie = {}
    if movie_title and genre and rating:
        new_movie["title"] = movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie 

    else:
        return None

def add_to_watched(user_data, movie):
    watched = user_data["watched"].append(movie)
    return user_data
    
    

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"].append(movie)
    return user_data

# def watch_movie(user_data, movie_title):
#     for key, value  in user_data.items():
#         user_data["watched"][0] = user_data["watchlist"][0]
#         user_data["watchlist"][0] = []
#         return user_data

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            
    return user_data

def get_watched_avg_rating(user_data):
    total = 0
    average = 0.0
    for movie in user_data["watched"]:
        if user_data["watched"] == 0:
          average = 0.0
          return average
        else:
          total += movie["rating"]
          average = (total / len(user_data["watched"]))
    return average  

def get_most_watched_genre(user_data):
    genres = []
    if len(user_data["watched"]) == 0:
        return None  
    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    most_watched = max(genres)
    return most_watched


def get_unique_watched(user_data):
    unique_movies = []
    friends_movies = []
    for friend in user_data["friends"]:
        for title in friend["watched"]:
            friends_movies.append(title)
    for movie in user_data["watched"]:
        if movie not in friends_movies:
            unique_movies.append(movie)
       
    return unique_movies

def get_friends_unique_watched(user_data):
    amanda = []
    friends_movies = []
    unique_friends = []
    totally_unique = []
    for title in user_data["watched"]:
        amanda.append(title)
    for titles in user_data["friends"]:
        if titles["watched"] not in amanda:
            friends_movies += titles["watched"]
    unique_friends = [i for i in amanda + friends_movies if i not in amanda]
    for unique in unique_friends:
        if unique not in totally_unique:
            totally_unique.append(unique)
    
    return totally_unique
    
def get_available_recs(user_data):
    recs = []
    seen = []
    recs_no_doops = []
    for movie in user_data["subscriptions"]:
        seen.append(movie)
        for friend in user_data["friends"]:
            for title in friend["watched"]:
                if title["host"] in movie:
                    recs.append(title)
    for r in recs:
        if r not in recs_no_doops:
            recs_no_doops.append(r)
    return recs_no_doops


def get_new_rec_by_genre(user_data):
    recs = []
    sonya = []

    for movie in user_data["watched"]:
        sonya.append(movie)
    #     if len(sonya) == 0:
    #         break
        
    # return recs
    for friend in user_data["friends"]:
        for genre in friend["watched"]:
            if genre not in sonya:
                recs.append(genre)
    if len(sonya) == 0:
        recs = []
    return recs

def get_rec_from_favorites(user_data):
    favs = []
    sonyas = []
    fav_rec = []
    unique_fav_rec = []

    for movie in user_data["favorites"]:
        favs.append(movie)
        for movie in user_data["watched"]:
            sonyas.append(movie)
    for friend in user_data["friends"]:
        fav_rec.append(friend["watched"])
        fav_rec += friend["watched"]
    

    for f in favs:
        if f in sonyas:
            unique_fav_rec.append(f)
        if f in fav_rec:
            unique_fav_rec.remove(f)

    return unique_fav_rec
        






        



    

    
