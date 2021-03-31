
#------------------------Wave 1--------------------------------------------------------------------------
def create_movie(title, genre, rating):

    #evaluate if any of these conditions are true then create a movie dictionary
    if (title) and (genre) and (rating):
        new_movie = {"title" : title, "genre" : genre,  "rating" : rating } 
        return new_movie
    
    #if even one of the 3 criterias are not met then return none    
    elif (not title) or (not genre) or (not rating):
        return None
    #for any other variety of critera too return none
    else:
        return None
    
def add_to_watched(user_data, new_movie):
    #add the new movie to the users data's watched dictionary
    user_data["watched"].append(new_movie)

    return user_data

def add_to_watchlist(user_data, movie):

    #add movie to the user data's watchlist dctionary
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    #iterate over the user_data's watchlist (which is a dictionary)
    for watchlist_movie in user_data["watchlist"]:
        #evaluate if the title input is equal to the title in the watchlist dict for each movie
        if title == watchlist_movie["title"]:
            #if title is found then remove this movie from the users watchlist dictionary
            user_data["watchlist"].remove(watchlist_movie)
            #and add to the watched movie dictionary
            add_to_watched(user_data, each_movie)
            return user_data  
        
    return user_data

#---------------------------------------------WAVE 2----------------------------------------

def get_watched_avg_rating(user_data):
    #initialise the variables that will store value
    sum_of_ratings = 0
    average_rating = 0
    #create a variable that holds the users watched data dictionary of movies
    watched_list = user_data["watched"]

    #guard clause to handle bad data
    if(len(watched_list) == 0):
        return 0.0
    
    #get the ratings from the users watched movie dictionary and get the total
    for watched_movie in watched_list:
        #as it iterates it finds the ratings and does the calculation below
        sum_of_ratings += watched_movie["rating"]

    #steps out of the loop to calculate the average once the total sum is calculated
    #average will be the sum divided by the length of the watched list
    list_length = len(watched_list)
    average_rating = sum_of_ratings / list_length

    return (float(average_rating))


def get_most_watched_genre(user_data):
    
    #create a variable to store the list of movie dictionaries in the users watched dictionary
    watched_list = user_data["watched"]

    #guard clause
    if(len(watched_list) == 0):
        return None

    # keep a count of the frequency of that genre, this dict will store the genre values as keys and the 
    #number of times they repeat as the values so, genre_count = {"fantasy": 1, intrigue:3}
    genre_count = {}

    # Iterate over the watched movie list and populate the genre_counts dict
    for movie in watched_list:
        genre = movie["genre"]
        # if the genre does not exist in the genre_counts dict, initialize it to 0
        #genre_count keys is the same a s
        if (genre not in genre_count.keys()):
            #populate the genre_count dict: add this key value pair 
            genre_count[genre] = 0
        
        # for every one genre_count that gets populated add 1 to reflect the number of times it appears in this dictionary
        genre_count[genre] += 1
        
    # find the nax value of the genre_counts.values() ==> max frequency
    maximum_genre_counts = max(genre_count.values())

    # Find the genre name that corresponds to the max frequency count
    for genre in genre_count:
        if genre_count[genre] == maximum_genre_counts:
                 
    # return genre_name
            return genre       

    return None

#----------------------------WAVE 3----------------------------------------------------------------------

def get_unique_watched(user_data):
    #create a copy of the users watched data as i will remove items from it and dont want it to affect the 
    #original data
    users_watched_movies_copy = user_data["watched"].copy()
    
    #iterate over the user_data's friends dictionary
    for friend_dict in user_data["friends"]:
        
        #create a new variable to store the friends watched dictionary
        friend_movies_list = friend_dict["watched"]
        
        #iterate over the friends watched movie list to get the elements which is in dict format
        for friend_movie in friend_movies_list:
            
            #if the movie exists in the list call the helper funtions with the given parameters is true then:
            if (does_movie_exist_in_list(friend_movie["title"], users_watched_movies_copy)):
                
                #then remove the movie by calling the helper function
                remove_duplicate_movie_from_list(friend_movie["title"], users_watched_movies_copy)
    
    return users_watched_movies_copy         


def get_friends_unique_watched(user_data):
    #initailize an empty list to store the output
    friends_unique_watched = []
    
    #create a new variable to store the users watched dictionaries
    users_watched_movies = user_data["watched"]
    
    #iterate over the users friends data to ge the friends dictionary 
    for friend_dict in user_data["friends"]:
        
        #create a new variabe to store the friends watched list of dictionaries
        friend_movies_list = friend_dict["watched"]
        
        #iterate over the friends watched list of dictionary (each element is a dictionary)
        for friend_movie in friend_movies_list:
            
            #call the helper function to check if the statement is true: if the movie does not exist is false
            if (not does_movie_exist_in_list(friend_movie["title"], users_watched_movies)):
                
                #then call the helper function with the given parameters to add the friend movie to the list
                add_movie_to_list(friend_movie, friends_unique_watched)
    
    return friends_unique_watched  
      
#helper functions
def does_movie_exist_in_list(movie_title, movie_list):
    for mov in movie_list:
        if (mov["title"] == movie_title):
            return True
    
    return False       
#helper function
def add_movie_to_list(movie, movie_list):
    if (not does_movie_exist_in_list(movie["title"], movie_list)):
        movie_list.append(movie)

#helper function
def remove_duplicate_movie_from_list(movie_title, movie_list):
    for movie in movie_list: 
        if movie['title'] == movie_title: 
            del movie_list[i] 
            return

#-------------------------------------WAVE 4----------------------------------------------------------- 
def get_available_recs(user_data):
    
    #2 criterias:
    # At least one friend has watched the movie
    # The friends movie's host == user's subscription
	#initialize a new list variable
    users_recommended_movie_list = []
    
    users_watched_movies = user_data["watched"]

    #iterate over all the movies in each friends watched list
		
	#iterates over each friend
    for friend_dict in user_data["friends"]:
        
        friend_movies_list = friend_dict["watched"]
        
		#iterates over a friend's movie list
        for friend_movie in friend_movies_list:
            
            if (not(does_movie_exist_in_list(friend_movie["title"], users_watched_movies)) and
                    is_movie_host_in_subscription_list(friend_movie["host"], user_data["subscriptions"])):

                #call the function with the friend_movie dict and the output list of recommended movies
                add_movie_to_list(friend_movie, users_recommended_movie_list)
    
    return users_recommended_movie_list     


#this function takes a movie host and subscription list and checks if the movie host exists in the subscription list (reusable for any other function)
def is_movie_host_in_subscription_list(movie_host, subscription_list):
    
    #subscription_list is just a list of string, where each element is a subscription
    for sub in subscription_list:
        if (sub == movie_host): 
            return True
    
    return False


##-----------------------------WAVE 5-----------------------------------------------------------------   

def get_new_rec_by_genre(user_data):
    
    #initialize a new list for the output movie
    list_of_recommended_movies = []
    
    #assign a variable to the function called for the most watched genre, and friends unique watched
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched_list = get_friends_unique_watched(user_data)
     
    #iterate over the user_data friends dict    
    for friends_dict in user_data["friends"]:
        
        #iterate over the friends watched movies dictionary 
        for friends_watched in friends_dict["watched"]:
            
            #evaluate if the most popular genre is present in the friends watched movies genre, if it's true
            if most_watched_genre == friends_watched["genre"]:
                
                    #append the movie dictionary associated with the genre to the output list
                    list_of_recommended_movies.append(friends_watched)
                   
                    
    return list_of_recommended_movies
                    
def get_rec_from_favorites(user_data):

#create a copy of the users watched data as i will remove items from it and dont want it to affect the 
    #original data
    list_of_recommended_favorite_movies = user_data["favorites"].copy()
    
    #iterate over the user_data's friends dictionary
    for friend_dict in user_data["friends"]:
        
        #create a new variable to store the friends watched dictionary
        friend_movies_list = friend_dict["watched"]
        
        #iterate over the friends watched movie list to get the elements which is in dict format
        for friend_movie in friend_movies_list:
            
            #if the movie exists in the list call the helper funtions with the given parameters is true then:
            if (does_movie_exist_in_list(friend_movie["title"], list_of_recommended_favorite_movies)):
                
                #then remove the movie by calling the helper function
                remove_duplicate_movie_from_list(friend_movie["title"], list_of_recommended_favorite_movies)
    
    return list_of_recommended_favorite_movies  
    
    
''' def get_rec_from_favorites(user_data): #second approach    
#initialize the new list of recommended movies
    list_of_recommended_favorite_movies = []
    list_of_friends_watched_movies = []
    #create a variable to store the list of dictionary of users favorites 
    
    if not user_data["favorites"]:
        return None
    
    #create a variable to store the list of dictionary of friends watchlist    
    for friends_list in user_data["friends"]:
        for friends_mov in friends_list["watched"]:
           list_of_friends_watched_movies.append(friends_mov)
    
    #iterate over the movies in the users fav movie dict
    for movies in user_data["favorites"]:
        if movies not in list_of_friends_watched_movies:
            list_of_recommended_favorite_movies.append(movies)
            
    return list_of_recommended_favorite_movies       ''' 
       
''' def get_all_friends_watched_mov(user_data):
    for friends_list in user_data["friends"]:
        for friends_mov in friends_list["watched"]:
        list_of_friends_watched_movies.append(friends_mov) d '''
       
       
