
def create_movie(title, genre, rating):
    if title == None:
        return None
    elif genre == None:
        return None
    elif rating == None: 
        return None
    else:
        movie_dict = {
            'title': title, 
            'genre': genre, 
            'rating': rating
        } 
    print("movie dictionary:",movie_dict)
    return movie_dict

def add_to_watched(user_data, movie):

    '''
    the value of `movie` will be a dictionary in this format:
    
      {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
      }
    '''
    #the value of `user_data` will be a dictionary \n
    #  with a key `"watched"`, and a value `[]`
    user_data["watched"] = []
    user_data["watched"].append(movie)
    return user_data

# Test 3
def add_to_watchlist(user_data,movie):
   # movie["title"]
    # print("movie:", movie)
    user_data_watchlist = user_data["watchlist"]
    # print("user")
    user_data["watchlist"].append(movie)
    return user_data
#Test 4

def watch_movie(user_data,title):
    #iterate through the watchlist of the user
    for movie in user_data["watchlist"]:
        # print("movie:", movie)
        if movie["title"] == title:
            #add to watched list
            user_data["watched"].append(movie) 
            #remove from watch list 
            user_data["watchlist"].remove(movie)  
            # print(user_data)
    return user_data
                  


#Wave 3 
"""
# - Consider the movies that the user has watched, and  consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies
"""
def get_unique_watched(user_data):
    if not user_data["watched"]:
        return []
    
    # get movies watched by user
    # get movies watched by friends
    # get unique movies the user has watched but friends have not watched.  
    # compare movies watched by friends to amanda's watched
    user_watched_movie_titles = user_data["watched"]
    friends_watched_movie_titles = user_data["friends"]
    user_unique_movies_titles = []
    # for movie in amanda_watched_movie_titles:
       
    #FOR name_of_individual_thing_in_array IN array_you_want_to_loop_through:
    for title in user_watched_movie_titles: 
        count = 0 #unique movie is Zero
        for friend in friends_watched_movie_titles: 
            if count > 0:
                break 
            if title in friend["watched"]:
                count += 1
        if count == 0:    
            user_unique_movies_titles.append(title)    
     
    return user_unique_movies_titles # list of dictionaries



def get_watched_avg_rating(user_data):
    #user_data = { 'watched': [{..},{..}] }
    var_watched = user_data["watched"]
    if user_data["watched"] == []:
        return 0
    #var_watched = [ {..} , {..} ]
    rating_sum = 0.0
    rating_avg = 0.0
    
    for element in var_watched: 
        # element = {...} , {...} , {...} //Now you get each element in the list
        #element = { 'genre': , 'rating':, 'title':}
        # print("element:", element)
        my_rating = element['rating'] # 4.8 or 2.0 or 3.9
        
        if my_rating == None:
            my_rating = 0.0
        # print("my_rating:",my_rating )
        rating_sum += my_rating
        # print("rating_sum:", rating_sum)
    
    rating_avg = rating_sum/len(var_watched)   
    # print("rating_avg:", rating_avg) # 0
    return rating_avg

#does this parameter have to be the exact name
def get_most_watched_genre(user_data):
    # print(user_data)
    if user_data["watched"] == []:
        return None
    movie_type = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        # print("genre:", genre)
        if genre not in movie_type:
            movie_type[genre] = 1
        else:
            movie_type[genre] +=1

    print("$$$$$$$$$$$$$$:0", movie_type)
     # [i]["genre"]
    
    # print(movie_type)
    most_watched_genre_key = max(movie_type, key = movie_type.get)
    print(most_watched_genre_key)
    return most_watched_genre_key




def get_friends_unique_watched(user_data):
    movie_list_of_dict = []
    user_movies = user_data["watched"]
    friends = user_data["friends"]
    for friend in friends:
        movie_lst_friend_watched = friend["watched"]
        for element in movie_lst_friend_watched:
            # print()
            if element not in user_movies and element not in movie_list_of_dict:
                # {"title": "Title A"}
                # print(f"{} is unique")
                movie_list_of_dict.append(element)
        # print("movie_list_of_dict>>", movie_list_of_dict)
    return movie_list_of_dict

#Wave 4   

def get_available_recs(user_data):
    friends_watched_movie_titles = get_friends_unique_watched(user_data)
    print("############################")
    print("friends_watched_movie_titles>>",friends_watched_movie_titles)
    print("############################")
    # recommendations = [{"title":[],"host":[]}]
    recommendations = []

    for movie in friends_watched_movie_titles:  
        #movie = {title1, host1}
        if movie["host"] in user_data['subscriptions']:
            recommendations.append(movie)
    
    print(recommendations)
    return recommendations


#Wave 5  Get recommendations by genre
def get_new_rec_by_genre(user_data):
    recommendation = []
    final_recommendation = []
    user_movies = user_data["watched"]

    # print("user_movies>>",user_movies)
    # print()
    friends_list = user_data["friends"]
    # print("friends>>",friends_list)
    # print()
    # most frequently watched genre
    fav_genre = get_most_watched_genre(user_data)
    # print("fav_genre>>> ", fav_genre)
    if user_movies == []:
        return []
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie["genre"] == fav_genre and movie not in user_movies:
                recommendation.append(movie)
    return recommendation

def get_rec_from_favorites(user_data):
    # - The movie is in the user's `"favorites"`
    # - None of the user's friends have watched it
    # - Return the list of recommended movies
    friends = user_data["friends"]
    user_movies = user_data["watched"]
    user_favorites = user_data["favorites"]
    recommendation = []
    if friends == []:
        return []
    # if user_movies == []: # and no unique movies
    #     return []

    for favorite in user_favorites:
        if favorite in user_movies:
            has_been_watched_by_friends = False
            for friend in friends:
                if favorite in friend["watched"]:
                    has_been_watched_by_friends = True
                    break
            if has_been_watched_by_friends == False:
                recommendation.append(favorite)
    return recommendation


    













    