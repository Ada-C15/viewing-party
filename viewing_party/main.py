def create_movie(title, genre, rating):

    #updated_data= {}
    #movie_to_watch = {}
   
    if (title) and (genre) and (rating):
        new_movie = {"title" : title, "genre" : genre,  "rating" : rating } 
        return new_movie
        
    elif (not title) or (not genre) or (not rating):
        return None

    else:
        return None
    
def add_to_watched(user_data, new_movie):

    #user_data = {"watched": []}

    user_data["watched"].append(new_movie)

    return user_data

def add_to_watchlist(user_data, movie):

    #user_data = { "watchlist": []}

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    #user_data = { "watchlist": [],
                  # "watched" : []}
    for watchlist_movie in user_data["watchlist"]:
        if title == watchlist_movie["title"]:
            user_data["watchlist"].remove(watchlist_movie)
            user_data["watched"].append(watchlist_movie)
            return user_data  #breaking because it has found the movie and it does not need to iterate over the list.
        
    return user_data

# WAVE 2

def get_watched_avg_rating(user_data):

    sum_of_ratings = 0
    average_rating = 0
    watched_list = user_data["watched"]

    if(len(watched_list) == 0):
        return 0.0

    for watched_movie in watched_list:

        sum_of_ratings = sum_of_ratings + watched_movie["rating"]

    list_length = len(watched_list)
    average_rating = sum_of_ratings / list_length

    return (float(average_rating))


def get_most_watched_genre(user_data):

    watched_list = user_data["watched"]

    if(len(watched_list) == 0):
        return None

    # Create dict genre_counts with key as genre name and value as frequency of that genre
    genre_count = {}

    # Iterate over the watched movie list and populate the genre_counts dict
    for movie in watched_list:
        genre = movie["genre"]
        # if the genre does not exist in the genre_counts dict, initialize it to 0
        if (genre not in genre_count.keys()):
            genre_count[genre] = 0
        
        # Add one to increment the frequency count for that genre
        genre_count[genre] += 1
        
    # find the nax value of the genre_counts.values() ==> max frequency
    maximum_genre_counts = max(genre_count.values())

    # Find the genre name that corresponds to the max frequency count
    for genre in genre_count:
        if genre_count[genre] == maximum_genre_counts:
                 
    # return genre_name
            return genre       

    return None

#WAVE 3

def get_unique_watched(user_data):
    
    users_watched_movies_copy = user_data["watched"].copy()
    
    for friend_dict in user_data["friends"]:
        
        friend_movies_list = friend_dict["watched"]
        
        for friend_movie in friend_movies_list:
            
            if (does_movie_exist_in_list(friend_movie["title"], users_watched_movies_copy)):
                remove_movie_from_list(friend_movie["title"], users_watched_movies_copy)
    
    return users_watched_movies_copy         


def get_friends_unique_watched(user_data):
    
    friends_unique_watched = []
    
    users_watched_movies = user_data["watched"]
    
    for friend_dict in user_data["friends"]:
        
        friend_movies_list = friend_dict["watched"]
        
        for friend_movie in friend_movies_list:
            
            if (not does_movie_exist_in_list(friend_movie["title"], users_watched_movies)):
                add_movie_to_list(friend_movie, friends_unique_watched)
    
    return friends_unique_watched         

def does_movie_exist_in_list(movie_title, movie_list):
    for mov in movie_list:
        if (mov["title"] == movie_title):
            return True
    
    return False       

def add_movie_to_list(movie, movie_list):
    if (not does_movie_exist_in_list(movie["title"], movie_list)):
        movie_list.append(movie)

def remove_movie_from_list(movie_title, movie_list):
    for i in range(len(movie_list)): 
        if movie_list[i]['title'] == movie_title: 
            del movie_list[i] 
            return



def get_unique_watched_sne(user_data):
    #creat an empty dict to store the new movie list 
    unique_user_watch_list = []

    
    #create variables that store the list of movies
    user_watched_movie_list = user_data["watched"]
    friends_watched_movie_list = user_data["friends"]

    number_of_friends = len(friends_watched_movie_list)

    #iterate over the user watched movie list and compare with friends movies
    for movies_dict in user_watched_movie_list:
        
        count_of_friends_seen_movie = 0
        
        for friends_movies_dict in friends_watched_movie_list:
            for friend_watched_movies in friends_movies_dict["watched"]:
                # a friend has seen this movie 
                if movies_dict["title"] == friend_watched_movies["title"]:
                    count_of_friends_seen_movie += 1
                    break # go to the next friend 
                           
        # at this point, none of the friends has seen this movie
        if (count_of_friends_seen_movie == 0):
            add_movie_to_list(movies_dict, unique_user_watch_list)

    return unique_user_watch_list

def get_friends_unique_watched_sne(user_data):

    unique_friend_watch_list = []

    user_watched_movie_list = user_data["watched"]
    friends_watched_movie_list = user_data["friends"]

    
    for friends_movies_dict in friends_watched_movie_list:
        for movies_dict in user_watched_movie_list:
            for user_watched_movies in movies_dict["watched"]:
        
                if friends_movies_dict["title"] != user_watched_movies["title"]:
                    unique_friend_watch_list.append(friends_movies_dict)
        
    return unique_friend_watch_list
    
    return len(unique_friend_watch_list)








# test program starts here
""" new_movie1 = create_movie("m1", "ab", 3)
new_movie2 = create_movie("m2", "ac", 4)
new_movie3 = create_movie("m3", "ad", 2)
new_movie4 = create_movie("m4", "aef", 1)

user_data = { "watchlist": [new_movie1, new_movie2, new_movie3, new_movie4],
            "watched" : [new_movie1, new_movie2, new_movie3, new_movie4]}
    
get_most_watched_genre(user_data) """