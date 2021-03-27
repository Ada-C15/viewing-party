#Test_wave_1
#checking four tests in create_movie function 
def create_movie(title, genre, rating):
    """
    checks if three given parameter is True or False 
    input: Three parameters(title, genre, rating)
    output: dict values or None 
    """

    if title and genre and rating:
        movies = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
        return movies
    else:
        return None 

#checks one test 
def add_to_watched(user_data, movie):
    """
    Adds dict to "watched"
    input: Two parameters(user_data, movie)
    output: updates data 
    """
    user_data["watched"].append(movie)
    return user_data

#checks one test 
def add_to_watchlist(user_data, movie):
    """
    Adds dict to watchlist 
    input: two parameters(user_data, movie)
    output: updates data 
    """
    user_data["watchlist"].append(movie)
    return user_data

#There are three tests in watch_movie function 
def watch_movie(user_data, movie):
    """
    stores data from "watchlist" to "watched"
    input: two paramemters(user_data, movie)
    output: returns updated data  
    """
    
    for element in user_data["watchlist"]:
        if movie == element["title"]:

            user_data["watched"].append(element)
            user_data["watchlist"].remove(element)
    return user_data


#Test_wave_2------------------------------

#checks two tests on this function 
def get_watched_avg_rating(user_data):
    """
    Getting an average of "watched" movie rating
    input: user_data
    output: average of "watched" movie rating 
    """
    sum_rating = []
    #len_rating = []
    if user_data["watched"]:
        for movie in user_data["watched"]:
            sum_rating.append(movie["rating"]) 
        return sum(sum_rating)/len(sum_rating)
    else: 
        return 0 

#checks two tests on this function 
def get_most_watched_genre(user_data):
    """
    Returns most "watched" genre
    input: user_data
    output: most "watched" genre
    """
    genre_dict = {} #all genre dict
    
    if user_data["watched"]:
        for movie in user_data["watched"]:
            genre = movie["genre"]  
            if genre not in genre_dict:
                genre_dict[genre] = 1
            else: 
                genre_dict[genre] += 1

        count = 0 
        max_genre = None 
        for genre, genre_count in genre_dict.items(): #genre_count are values
            if genre_count > count:
                count = genre_count 
                max_genre = genre 
        return max_genre 
  
    else:
        return None 

#Wave_3-----------------------------

#two tests in this function 
def friend_watched_list(user_data):
    """
    create list of friend watched list
    input: user_data
    output: friend watched list 
    """
    friend_watched = []

    for friend in user_data["friends"]:
        #for movies in friend.values():
        movies = friend["watched"]
        for movie in movies:
            friend_watched.append(movie)
    return friend_watched

def get_unique_watched(user_data):
    """
    creates a list of movies friends haven't watched 
    input: user_data
    output: unique watched 
    """
    unique_watched = []
    user_watched = user_data["watched"]
    friend_watched = friend_watched_list(user_data)
    
    for movie in user_watched:
        if movie not in friend_watched and movie not in unique_watched:
            unique_watched.append(movie)
    return unique_watched


#two tests in this function 
def get_friends_unique_watched(user_data):
    """
    creates friends unique watched 
    input: user_data
    output: unique watched 
    """

    user_watched = user_data["watched"]
    unique_watched = []
    
    friend_watched = friend_watched_list(user_data)

    for movie in friend_watched:
        if movie not in user_watched and movie not in unique_watched:
            unique_watched.append(movie)
    return unique_watched


#wave_4------------------------------------

#two tests in this function
def get_available_recs(user_data):
    """
    get available recs 
    input: user_data
    output: recommendated movie list 
    """
    list_of_recommendation = []
    streaming_services = user_data["subscriptions"]

    for friend in user_data["friends"]:
        for movies in friend.values():
            for movie in movies:
                if movie["host"] in streaming_services and movie not in list_of_recommendation:
                    list_of_recommendation.append(movie)
    return list_of_recommendation


#wave_5---------------------------------------

#four test in this function 
def get_new_rec_by_genre(user_data):
    """
    recomends new movies by genre 
    input: one paramemter(user_data)
    output: recommendated movie list 
    """
    most_watched = get_most_watched_genre(user_data)
    recs_finding_genre = get_friends_unique_watched(user_data) 
    recs_genre = []

    for movie in recs_finding_genre:
        if most_watched in movie.values():
            recs_genre.append(movie)
    return recs_genre


#one test in this function 
def get_rec_from_favorites(user_data):
    """
    recomonds new movies looking at favorites 
    input: user_data
    output: list of movies from favorities 
    """
    find_fav_rec = user_data["favorites"]

    friend_watched = friend_watched_list(user_data)

    rec_fav = []

    for movie in find_fav_rec:
        if movie not in friend_watched:
            rec_fav.append(movie)
    return rec_fav