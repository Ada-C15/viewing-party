# WAVE 1 


def create_movie(title, genre, rating):
    movies = {
        "title":title,
        "genre":genre,
        "rating": rating
    }
    if title and genre and rating:
        return movies
    return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
            
    return user_data



# WAVE 2
#1

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    rate_sum = 0 
    if len(watched_list) == 0:
        return 0
    for movie_info in watched_list:
        rate_sum += movie_info["rating"]
        # print(movie_info)

    average_rating = rate_sum / len(watched_list)
    return average_rating 



#2
def calculate_genre_freq(watched):
    genre_freq_dict = {}
    # print(user_data)
    # print(user_data["watched"])
    # watch_list = user_data["watched"]
    for movie in watched:
            genre = movie["genre"]
            if genre in genre_freq_dict.keys():
                genre_freq_dict[genre] += 1 

            else:
                genre_freq_dict[genre] = 1

    return genre_freq_dict



def get_most_watched_genre(user_data):  
    # print(user_data)
    # print(user_data["watched"])

    watched = user_data["watched"]
    genre_freq_dict = calculate_genre_freq(watched)
    most_popular = 0
    most_popular_genre = ""
    # print("before the loop")
    #what if there was an empty list 
    if len(watched) == 0:
        return None
    for key,value in genre_freq_dict.items():
        if value > most_popular:
            most_popular = value
            most_popular_genre = key  
    # print("after the loop")             
    return most_popular_genre
            





#WAVE 3 

def get_unique_watched(user_data):
# we need to compare the watched lists for both the
    # user and the freinds 
    # find which movies friends haven't watched 
    # but the user has 
    # return a list of dict that shows these movies? 
    # also add in if the list is empty 
    
    # user_watched_movies = [] #will hold the value of ["title"]
    friends_watched_movies = [] #will hold the value of ["title"] 
    user_unique_titles = [] #movies that we ended up comparing and the user had watched
    
    # for movie in user_data["watched"]:
    #     user_watched_movies.append(movie["title"])       


    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movies.append(movie)
    
    
    #need to loop through unique watched movies 
    # for unique_movies in user_data["watched"]
    for unique_movies in user_data["watched"]:
        if unique_movies not in friends_watched_movies:
            user_unique_titles.append(unique_movies)
    
    return user_unique_titles


#  to help if you want to use sets ??  
# >>> {1, 2, 3, 4} - {2, 3}
# {1, 4} 



def get_friends_unique_watched(user_data):
    # user_watched_movies = []
    friends_watched_movies = []
    unique_watched_movies = []

    # for movie in user_data["watched"]:
    #     user_watched_movies.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movies.append(movie)
    

    
    for movie in friends_watched_movies:
        if movie not in user_data["watched"]:
            if movie not in unique_watched_movies:
                unique_watched_movies.append(movie)
    
    
    
    return unique_watched_movies    

        
    
    # one friend has watched but the user has NOT watched
    # for unique_movie in unique_watched_movies: 
            




#WAVE 4

def get_available_recs(user_data):
    # movies the user has not watched(can access via their sub) but a friend has watched
    recommended_movies = []

    # wave 3 function that returns the unique watched movie list
    # why isn't there a test to check if the user hasn't watched the movie but their friends have? 
    # unique_movie = get_friends_unique_watched(user_data) 
    streaming_services = user_data["subscriptions"]




    for friend in user_data["friends"]:
        for movies in friend.values():
            for movie in movies: 
                    if movie["host"] in streaming_services and movie not in recommended_movies:
                        recommended_movies.append(movie)
    


    return recommended_movies 



# WAVE 5 

def get_new_rec_by_genre(user_data):
    rec_movies = []
    popular_genre = get_most_watched_genre(user_data)
    unique_movie = get_friends_unique_watched(user_data)

    #   for movie in unique_movie:
    #     if popular_genre in movie.values():
    for movie in unique_movie:
        if popular_genre in movie.values():
            rec_movies.append(movie)
    return rec_movies



def get_rec_from_favorites(user_data): 
    rec_movies = []
    # popular_genre = get_most_watched_genre(user_data)
    friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    
    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            rec_movies.append(movie)

    return rec_movies