#--------FUNCTIONS FOR WAVE01--------#

def create_movie(movie_title, genre, rating):
    #If movie title, genre or rating are None, then return None
    if not movie_title or not genre or not rating:
        return None
    #Create a movie dictionary and return it
    movie_dictionary = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating
    }
    return movie_dictionary

def add_to_watched(user_data, movie):
    #User adds a movie to the list value of "watched" key.
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #User adds a movie to the list value of "watchlist" key.
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #Watchlist key value (list), will be stored in watchlist_list 
    # and then iterated.
    watchlist_list = user_data["watchlist"]
    #Each element of that list is a movie represented with a 
    # dictionary containing the keys: title, genre and rating. 
    for movie in watchlist_list:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            watchlist_list.remove(movie)
    return user_data


#--------FUNCTIONS FOR WAVE02--------#

def get_watched_avg_rating(user_data):
    #Initialize a counter in 0
    movies_rating = 0
    movies_watched_list = user_data["watched"]
    #If watched movies list is empty, return 0.0 as average
    if len(movies_watched_list) == 0:
        return 0.0
    #If not empty, add each movie rating to the total (movies_rating)
    for movie in movies_watched_list:
        movies_rating += movie["rating"]
    return movies_rating / len(movies_watched_list)

'''
This function creates a genre dictionary to store the movie's
genre and how many times that gender has been watched.
OUTPUT: Returns the most frequent genre wanched (string).
'''
def get_most_watched_genre(user_data):
    #Initialize an empty dictionary, empty string and counter in 0
    genre_dictionary = {}
    most_frecuent_genre = ""
    most_frecuent_genre_amount = 0
    #Generate a list of movies watched by user
    movies_watched_list = user_data["watched"]
    #If this list is empty return None
    if not len(movies_watched_list):
        return None
    #Loop though the movies
    for movie in movies_watched_list:
        #Add a genre to the dictionary or increment the value by 1
        if movie["genre"] in genre_dictionary:
            genre_dictionary[movie["genre"]] += 1
        else:
            genre_dictionary[movie["genre"]] = 1
        #Compare the value of this genre with the most frequent
        if genre_dictionary[movie["genre"]] > most_frecuent_genre_amount:
            most_frecuent_genre_amount = genre_dictionary[movie["genre"]]
            most_frecuent_genre = movie["genre"]
    return most_frecuent_genre


#--------FUNCTIONS FOR WAVE03--------#

'''
This function was created for easier analysis and understanding of future functions.
OUTPUT: Return a dictonary where key are the titles of movies watched by 
any friend of user, and value is another dictionary with movie's info.
'''
def get_friends_movies_watched_titles(friends_list):
    #Initialize an empty dictionary
    movies_watched = {}
    for friend in friends_list:
        #Generate a list of movies watched by this friend
        movies_watched_list = friend["watched"]
        for movie in movies_watched_list:
            #Loop through movies and add each new title to the dictionary
            if movie["title"] in movies_watched:
                continue
            else:
                movies_watched[movie["title"]] = movie
    return movies_watched

'''
This function dermine movies watched by user but not by friends
OUTPUT: List of unique movies watched by user
'''
def get_unique_watched(user_data):
    friends_list = user_data["friends"]
    movies_watched_list = user_data["watched"]
    #Initialize an empty list
    user_unique_movies = []
    movies_watched_by_friends = get_friends_movies_watched_titles(friends_list)     
    #Loop through movies. Determine movies watched by user and compare if the 
    # title exists in the movies watched by friends dictionary
    for movie in movies_watched_list:
        title = movie["title"]
        if title in movies_watched_by_friends:
            continue
        else:
            user_unique_movies.append(movie)
    return user_unique_movies

'''
This function determine movies watched by at least one friend
but not by the user.
OUTPUT: List of movies watched by at least one friend   
'''             
def get_friends_unique_watched(user_data):
    friends_list = user_data["friends"]
    movies_watched_list = user_data["watched"]
    #Initialize an empty list
    to_watchlist_movies = []
    movies_watched_by_friends = get_friends_movies_watched_titles(friends_list) 
    #Iterate the dictionary to get the title for the movies watched by
    #friends and then search for that title in movies watched by user
    for friends_movie_title, friends_movie_info in movies_watched_by_friends.items():
        for movie in movies_watched_list:
            user_movie_title = movie["title"]
            if user_movie_title == friends_movie_title:
                #This friend's movie title has been watched by the user.
                #Then break the loop for this movie, and continue to 
                #compare with the next friend's movie.
                break
        else:
            #This else will be executed if the movie title was not watched 
            #by the user. Then add this friend's movie info to the final list.
            to_watchlist_movies.append(friends_movie_info)
    return to_watchlist_movies


#--------FUNCTIONS FOR WAVE04--------#

def get_available_recs (user_data):
    #Initialize an empty list
    recommended_movies = []
    #Get the list of movies watched by at least one friend but not by the user
    movies_watched_by_friends_list = get_friends_unique_watched(user_data)
    #Iterate through movies. Check if the host for every movie watched 
    # by friends is in the user's subscriptions. If so, add it to final list.
    for movie in movies_watched_by_friends_list:
        for host in user_data["subscriptions"]:
            if host == movie["host"]:
                recommended_movies.append(movie)
    return recommended_movies


#--------FUNCTIONS FOR WAVE05--------#

def get_new_rec_by_genre(user_data):
    #Initialize an empty list
    recommended_movies = []
    #Get the list of movies watched by at least one friend but not by the user
    movies_watched_by_friends_list = get_friends_unique_watched(user_data) 
    #Get the user's most frequently watched genre (string)
    most_frequently_watched_genre = get_most_watched_genre(user_data) 
    for movie in movies_watched_by_friends_list:
        #If the the genre of this friend's movie is equal to the most watched
        #genre by user, then add it to the final recommended list.
        if movie["genre"] == most_frequently_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    #Initialize an empty list
    recommended_movies = []
    #Get the list of movies watched by all friends
    movies_watched_by_friends_dic = get_friends_movies_watched_titles(user_data["friends"])
    #Iterate through movies. If a title has not been watched by a friend, 
    #add it to the final list.
    for movie in user_data["favorites"]:
        if movie["title"] not in movies_watched_by_friends_dic:
            recommended_movies.append(movie)
    return recommended_movies








