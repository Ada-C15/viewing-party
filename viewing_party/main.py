def create_movie(title, genre, rating):
    movie_dic = {}
    if title and genre and rating:
        movie_dic["title"] = title
        movie_dic["genre"] = genre
        movie_dic["rating"] = rating
        return movie_dic
    else:
        return None



def add_to_watched(user_data,movie):
        user_data["watched"].append(movie)
        return user_data


def add_to_watchlist(user_data, movie):
        user_data["watchlist"].append(movie)
        return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]

    for movie in watchlist:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            watchlist.remove(movie)
            

    return user_data
            
        
# print(wave 2 *********************************)

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    sum = 0
    average = 0
    
    if len(watched_list) == 0:
        return average

    for movie in watched_list:
        sum += movie["rating"]
        average = sum /len(watched_list)
    return average

def get_most_watched_genre(user_data):
    most_watched = user_data["watched"]

# what gender is most frequently occurring in the watched list.
# return genre
#  count how many times each genre shows up. counts of each genre.
    popular_genre = {}

    for movie in most_watched:
        genre = movie["genre"]
        if genre in  popular_genre:
            popular_genre[genre] += 1

        else:
            popular_genre[genre] = 1

    max = 0
    max_genre = None
    for genre, count in popular_genre.items():
        if count > max:
            max = count
            max_genre = genre
        


            
    return max_genre


# # print(wave3 ***************************) 
def make_friends_list(user_data):
    friends_list = []
    for friend_movie in user_data["friends"]: 
        for movie in friend_movie["watched"]:
           
#  some nesting to pull out the friends movies
                friends_list.append(movie)

    return friends_list

def get_unique_watched(user_data):

    friends_list = make_friends_list(user_data)
            
    # print(friends_list)

    movie_list = []
    for user_movie in user_data["watched"]:
        # print(user_movie)

        if user_movie not in friends_list:
            movie_list.append(user_movie)
    
    return movie_list


        
def get_friends_unique_watched(user_data):
    friends_list = make_friends_list(user_data)
                
            
    # print(friends_list)

    user_unwatched = []
    for friend_movie in friends_list:
        if friend_movie not in user_data["watched"] and friend_movie not in user_unwatched:
        # print(user_movie)
            user_unwatched.append(friend_movie)
    # print(user_unwatched)
    
    return user_unwatched




    


# # print(wave 4 *****************************)

def get_available_recs(user_data):

    recommended_movies = []
    friends_list = []
    for friend_movie in user_data["friends"]: 
        for host in friend_movie["watched"]:
            # if user_not_watched and friends_watched = 
            print(host)
            friends_list.append(host)
    
    for movie in friends_list:
        if movie not in user_data["watched"] and movie not in recommended_movies and movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies
            
    


# # print(wave 5 ********************************)

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    like_genre = get_most_watched_genre(user_data) 
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["genre"] == like_genre and friend_movie not in user_data["watched"] and friend_movie not in recommended_movies:
                recommended_movies.append(friend_movie)
    return recommended_movies
    



def get_rec_from_favorites(user_data):
    favorite_movie = user_data["favorites"]
    for movie in user_data["friends"]:
        for fave_movie in movie["watched"]:
            if fave_movie in user_data["favorites"]:
                favorite_movie.remove(fave_movie)

    return favorite_movie

    

