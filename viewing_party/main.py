#Wave 1 
def create_movie(title,genre,rating): 
    if (title and genre and rating): 
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    elif not title or not genre or not rating:
        return None
  
def add_to_watched(user_data,movie): 
    user_data["watched"].append(movie)
    return user_data 

def add_to_watchlist(user_data,movie):
    if movie not in user_data["watchlist"]: 
        user_data["watchlist"].append(movie)
    return user_data 

def watch_movie(user_data, title):

    for e in user_data["watchlist"]:
        if e["title"] == title:
            user_data["watchlist"].remove(e) 
            user_data['watched'].append(e)
    return user_data 
 

# Wave # 2

def get_watched_avg_rating(user_data): 
    watched = user_data["watched"]
    if len (watched) == 0:  
        return 0 

    total = 0 
    for  movie in watched:  
        total += movie["rating"]
    
    average = total/len(watched)
    return average 

def get_most_watched_genre(user_data): 
    most_watched = user_data["watched"]

    all_genres = {}
    
    for movie in most_watched: 
        if movie["genre"] not in all_genres: 
            all_genres [movie["genre"]] = 1

        else: 
            all_genres [movie["genre"]] += 1


    max_count = 0 
    max_genre = None 
    for genre in all_genres: 
        count = all_genres[genre]
        if count > max_count: 
            max_count = count 
            max_genre = genre 

    return max_genre 

        

# Wave 3 

        
def get_unique_watched(user_data): 
    unique_watched = []
    all_friends_movies = []
    for friend in user_data['friends']:
        for m in friend['watched']:
            if m not in all_friends_movies:
                all_friends_movies.append(m)
    
    
    for movie in user_data["watched"]:
        if movie not in all_friends_movies:
            unique_watched.append(movie)

                 
    return (unique_watched)


def get_friends_unique_watched(user_data):
    friend_unique_watched = []
    all_friends_unique_movies = []
    for friend in user_data["friends"]: 
            for m in friend["watched"]: 
                if m not in all_friends_unique_movies: 
                    all_friends_unique_movies.append(m)
        
    for movie in all_friends_unique_movies: 
        if movie not in user_data["watched"]: 
            friend_unique_watched.append(movie)
            
    return (friend_unique_watched)

# Wave 4 

def  get_available_recs(user_data): 
    available_recs = []
    all_friends_recs = []
    unique_friends_watched = []
    friends_movie = get_friends_unique_watched(user_data)
    
    
    for m in friends_movie: 
        if m not in user_data["watched"]: 
            if m["host"] in user_data["subscriptions"]: 
                available_recs.append(m)

    return available_recs
    

# #Wave 5 

def get_new_rec_by_genre(user_data):  
    new_rec_by_genre = []
    friends_movie = get_friends_unique_watched(user_data)
    most_watched = get_most_watched_genre(user_data)


    for m in friends_movie: 
        if m["genre"] == most_watched: 
            if m not in user_data["watched"]: 
                new_rec_by_genre.append(m)

    return new_rec_by_genre

    
def get_rec_from_favorites(user_data):
    rec_from_favorites = []

    all_friends_movies = []
    for friend in user_data['friends']:
        for m in friend["watched"]:
            all_friends_movies.append(m) 
        #all_friends_movies.append(friend["watched"])

    for m in user_data["favorites"]: 
        if m not in all_friends_movies: 
            rec_from_favorites.append(m)

    return rec_from_favorites

    
