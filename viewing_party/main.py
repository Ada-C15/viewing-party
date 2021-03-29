#WAVE ONE

def create_movie(title, genre, rating):  
    movie_dict = {} 
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie) 
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #This represents that the user has a watchlist and\
    #a list of watched movies
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == title:
            user_data["watchlist"].remove(movie_dict)
            user_data["watched"].append(movie_dict)
            return user_data
    else:
        return user_data

#WAVE TWO

def get_watched_avg_rating(user_data):
    # the value of user_data will be a dictionary with a\
    #a "watched" list of movie dictionaries
    #This represents that the user has a list of watched\
    #movies
    avg_rating = 0.0
    count =0
    rating_sum = 0.0
    for movie_dict in user_data["watched"]:
        for key,value in movie_dict.items():
            if key == "rating":
                rating_sum += value
                count += 1
    #in place to settle division by zero error:
    if count == 0:
        avg_rating = 0
    else:
        avg_rating = rating_sum/count
    return avg_rating

def get_most_watched_genre(user_data):
    genre_count_dic ={}
    genre_count_list =[]
    for movie_dict in user_data["watched"]:
        for key,value in movie_dict.items():
            if key == "genre":
                genre_count_list.append(value)
    for x in genre_count_list:
        if not x in genre_count_dic:
            genre_count_dic[x] =1
        else:
            genre_count_dic[x] +=1

#obtain highest value in genre_count_dic 
#seperated key & value in two seperate lists
    k_list =[]
    v_list =[]
    for key,value in genre_count_dic.items():
        k_list.append(key)
        v_list.append(value)
#incase of an empty list returning None
    if len(k_list) == 0:
        genre_most = None
        return genre_most
    else:
        maximum = v_list[0]
        for x in v_list:
            if x > maximum:
                maximum= x 
#finding corresponding index of maximum value in key list
        g= v_list.index(maximum)
        genre_most = k_list[g]
        return genre_most

#WAVE THREE

def get_unique_watched(user_data):
    
    user_bank = []
    friends_bank =[]
    unseen_movies = {}
#user collection of watched movies
    for x in user_data["watched"]:
        for key,value in x.items():
            if key == "title":
                user_bank.append(value)
#friends collection of watched movies                
    for y in user_data["friends"]:
        for z in y["watched"]:
            for key, value in z.items():
                if key =="title":
                    friends_bank.append(value)
#Determine movies watched by user but not by friends
    teo =[]
    for x in user_bank:
        if x not in friends_bank:
            teo.append(x)
#Returning a list of dictionaries
    final_list = []
    for x in range(len(teo)):
        unseen_movies["title"] = teo[x]
        final_list.append(unseen_movies)
        unseen_movies = {}
    return final_list


def get_friends_unique_watched(user_data):
    user_bank = []
    friends_bank = []
    new_movie_for_user = []
#creating users watched list
    for x in user_data["watched"]:
        for key,value in x.items():
            if key == "title":
                user_bank.append(value) 
                
#creating friends watched list
    for y in user_data["friends"]:
        for z in y["watched"]:
            for key, value in z.items():
                if key =="title":
                    friends_bank.append(value)
#creating unique friend list removing duplicates
    unique_friend_list = []
    for x in friends_bank:
        if x not in unique_friend_list:
            unique_friend_list.append(x)
#comparing friends seen movies with user's movies
    teo =[]
    for x in unique_friend_list:
        if x not in user_bank:
            teo.append(x)
#returning a list of dictionaries \
# representing a list of movies
    unseen_movies = {}
    
    for x in range(len(teo)):
        unseen_movies["title"] = teo[x]
        new_movie_for_user.append(unseen_movies)
        unseen_movies = {}
    return new_movie_for_user

#WAVE FOUR

def get_available_recs(user_data):
    new_rec = get_friends_unique_watched(user_data)
    friends_bank_host =[]
    friends_bank_title =[]
    fin_mov =[]
    user_host =[]
#Retrieve Value in dictionary in new_rec
    for x in new_rec:
        for a,b in x.items():
            fin_mov.append(b)
#Finding host in recommended movies 
    for y in user_data["friends"]:
        for z in y["watched"]:
            for key,value in z.items():
                if z["title"] in fin_mov:
                    friends_bank_host.append(z["host"])
#Removing duplicate movies
    friends_bank_host_unique =[]
    for x in friends_bank_host:
        if x not in friends_bank_host_unique:
            friends_bank_host_unique.append(x)
#Creating a list of dictionaries   
    movie_rec ={}   
    movie_rec_list =[]  
    for x in range(len(fin_mov)):
        movie_rec["title"] = fin_mov[x]
        movie_rec["host"] = friends_bank_host_unique[x]
        movie_rec_list.append(movie_rec)
        movie_rec ={}
#Comparing host of rec movies is in the user's subscription    
    final_list_host = []
    for x in movie_rec_list:
        for key, value in x.items():
            if value in user_data["subscriptions"]:
                final_list_host.append(value)
#Appends movie from list of dictionaries
    final_list =[]
    for x in movie_rec_list:
        if x["host"] in final_list_host:
            final_list.append(x)
    
    return final_list

#WAVE FIVE
#1\
# Using previous functions, finding pop.genera of user
def get_new_rec_by_genre(user_data):
    most_genre = get_most_watched_genre(user_data)
    movie_rec = get_friends_unique_watched(user_data)
    genre_rec_unq =[]
    genre_rec = []
#if movie list or favorite genre is empty return emptylist
    if len(movie_rec) == 0:
        return genre_rec_unq
    elif most_genre == None:
        return genre_rec_unq
    else:
        for y in user_data["friends"]:
            for z in y["watched"]:
                for key,value in z.items():
                    if z["genre"] in most_genre:
                        genre_rec.append(z)
#Removing duplicate genres
        genre_rec_unq = []
        for x in genre_rec:
            if x not in genre_rec_unq:
                genre_rec_unq.append(x)
        return genre_rec_unq


def get_rec_from_favorites(user_data):
#Obtainig all movies watched by friends
    fav_list =[]
    friend_watched = []
    for x in user_data["friends"]:
        for y in x["watched"]:
            for a,b in y.items():
                friend_watched.append(b)
#Finding user fav not in friends watch list
    for x in user_data["favorites"]:
        if x["title"] not in friend_watched:
            fav_list.append(x["title"])
#Returning a list of recommended movies
    fav_list_rec_dict ={}
    fin_list_rec =[]
    for x in range(len(fav_list)):
        fav_list_rec_dict["title"] = fav_list[x]
        fin_list_rec.append(fav_list_rec_dict)
        fav_list_rec_dict ={}
    return fin_list_rec
    



