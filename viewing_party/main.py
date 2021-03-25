# Wave 1 start
def create_movie(movie_title,genre,rating):
    movie = {}
    if movie_title == None or genre == None or rating == None:
        return None
    else: 
        movie["title"] = movie_title
        movie["genre"] = genre
        movie["rating"] = rating
    print(movie)
    return movie

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return(user_data)

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return(user_data)

def watch_movie(user_data, movie):
    for elem in user_data['watchlist']:
        if movie == elem['title']:
            user_data['watchlist'].remove(elem)
            user_data['watched'].append(elem)
    return user_data 

# Wave 2 start
    
def get_watched_avg_rating(user_data):
    sum = 0.0
    avg = 0.0
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            sum+=movie["rating"]
            print(sum)
        avg = sum/len(user_data["watched"]) 
        return(avg)
    else:
        return 0

def get_most_watched_genre(user_data):
    genre_dict = {}
    if len(user_data) == 0 or len(user_data["watched"]) == 0:
        return None
    else: 
        for movie in user_data["watched"]:
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] +=1
            else:
                genre_dict[movie["genre"]] = 1
    # print(genre_list)
    maximum = max(genre_dict, key=genre_dict.get) 
    print(maximum)
    return(maximum)


# Wave 3

def get_unique_watched(user_data):
    user_set = set()
    friend_set = set()

    for user_movies in user_data["watched"]:
        user_set.add(user_movies["title"])
        
    for friend_items in user_data["friends"]:
            for movie in friend_items["watched"]:
                for title,val in movie.items():
                    friend_set.add(val)
    unique_set = user_set - friend_set
    
    unique_list = []
    for movie in unique_set:
        x = dict(title = movie)
        unique_list.append(x)
    return(unique_list)

def get_friends_unique_watched(user_data):
    user_set = set()
    friend_set = set()

    for user_movies in user_data["watched"]:
        user_set.add(user_movies["title"])
        
    for friend_items in user_data["friends"]:
            for movie in friend_items["watched"]:
                for title,val in movie.items():
                    friend_set.add(val)
    friends_unique_set = friend_set.difference(user_set) 
    # print(friends_unique_set) 

    friends_unique_list = []
    for movie in friends_unique_set:
        x = dict(title = movie)
        friends_unique_list.append(x)
    # return(unique_list)
    return(friends_unique_list)

# Wave 4
amandas_data = {
    "subscriptions": ["Service A", "Service B"],
    "watched": [],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title C",
                    "host": "Service C"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title B",
                    "host": "Service B"
                },
                {
                    "title": "Title D",
                    "host": "Service D"
                }
            ]
        }
    ]
}

def get_available_recs(user_data):
    # return a list of movies
    recommended_movies = []

    # Get var for subscriptions
    subs = user_data["subscriptions"]
    # determine which title in friends list matches user's services
    for friend_items in user_data["friends"]:
            for movie in friend_items["watched"]:
                if movie["host"] in subs and movie not in recommended_movies:
                    recommended_movies.append(movie)
    return(recommended_movies)

get_available_recs(amandas_data)