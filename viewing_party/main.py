#--------FUNCTIONS FOR WAVE01--------#

def create_movie(movie_title, genre, rating):
    '''
    This function initialize a dictionary with
    title, genre and rating
    '''
    if not movie_title or not genre or not rating:
        return None
    movie_dictionary = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating
    }
    return movie_dictionary

def add_to_watched(user_data, movie):
    '''
    This function receives a user and a movie,
    and adds the movie to the "watched" key of the user
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    This function receives a user and a movie,
    and adds the movie to the "watchlist" key of the user
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    This function receives a user and a movie.
    Adds the movie to the "watched" key of the user and
    removes it from the "watchlist" list.
    '''
    watchlist_list = user_data["watchlist"]
    for movie in watchlist_list:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            watchlist_list.remove(movie)
    return user_data


#--------FUNCTIONS FOR WAVE02--------#

def get_watched_avg_rating(user_data):
    '''
    This function receives a user and returns the 
    average rating for all the watched movies.
    '''
    movies_rating = 0
    movies_watched_list = user_data["watched"]
    if len(movies_watched_list) == 0:
        return 0.0
    for movie in movies_watched_list:
        movies_rating += movie["rating"]
    return movies_rating / len(movies_watched_list)


def get_most_watched_genre(user_data):
    '''
    This function creates a genre dictionary to store the movie's
    genre and how many times that gender has been watched.
    OUTPUT: Returns the most frequent genre wanched (string).
    '''
    genre_dictionary = {}
    most_frecuent_genre = ""
    most_frecuent_genre_amount = 0
    movies_watched_list = user_data["watched"]
    if not len(movies_watched_list):
        return None
    for movie in movies_watched_list:
        if movie["genre"] in genre_dictionary:
            genre_dictionary[movie["genre"]] += 1
        else:
            genre_dictionary[movie["genre"]] = 1
        if genre_dictionary[movie["genre"]] > most_frecuent_genre_amount:
            most_frecuent_genre_amount = genre_dictionary[movie["genre"]]
            most_frecuent_genre = movie["genre"]
    return most_frecuent_genre


#--------FUNCTIONS FOR WAVE03--------#

def get_friends_movies_watched_titles(friends_list):
    '''
    This function was created for easier analysis and understanding of future functions.
    OUTPUT: Return a dictonary where key are the titles of movies watched by 
    any friend of user, and value is another dictionary with movie's info.
    '''
    movies_watched = {}
    for friend in friends_list:
        movies_watched_list = friend["watched"]
        for movie in movies_watched_list:
            if movie["title"] not in movies_watched:
                movies_watched[movie["title"]] = movie
    return movies_watched


def get_unique_watched(user_data):
    '''
    This function dermine movies watched by user but not by friends
    OUTPUT: List of unique movies watched by user
    '''
    friends_list = user_data["friends"]
    movies_watched_list = user_data["watched"]
    user_unique_movies = []
    movies_watched_by_friends = get_friends_movies_watched_titles(friends_list)     
    for movie in movies_watched_list:
        title = movie["title"]
        if title not in movies_watched_by_friends:
            user_unique_movies.append(movie)
    return user_unique_movies


def get_friends_unique_watched(user_data):
    '''
    This function determine movies watched by at least one friend
    but not by the user.
    OUTPUT: List of movies watched by at least one friend   
    '''
    friends_list = user_data["friends"]
    movies_watched_list = user_data["watched"]
    to_watchlist_movies = []
    movies_watched_by_friends = get_friends_movies_watched_titles(friends_list) 
    for friends_movie_title, friends_movie_info in movies_watched_by_friends.items():
        for movie in movies_watched_list:
            user_movie_title = movie["title"]
            if user_movie_title == friends_movie_title:
                break
        else:
            to_watchlist_movies.append(friends_movie_info)
    return to_watchlist_movies


#--------FUNCTIONS FOR WAVE04--------#

def get_available_recs (user_data):
    '''
    This function determines a list of recommended movies.
    A movie should be added to this list if the user has not
    watched it, at least one of the user's friends has watched
    and the "host" of the movie is a service that is in
    the user's "subscriptions"
    '''
    recommended_movies = []
    movies_watched_by_friends_list = get_friends_unique_watched(user_data)
    for movie in movies_watched_by_friends_list:
        for host in user_data["subscriptions"]:
            if host == movie["host"]:
                recommended_movies.append(movie)
    return recommended_movies


#--------FUNCTIONS FOR WAVE05--------#

def get_new_rec_by_genre(user_data):
    '''
    This function determines a list of recommended movies. 
    A movie should be added to this list if the user has 
    not watched it, at least one of the user's friends has 
    watched and the "genre" of the movie is the same as 
    the user's most frequent genre
    '''
    recommended_movies = []
    movies_watched_by_friends_list = get_friends_unique_watched(user_data) 
    most_frequently_watched_genre = get_most_watched_genre(user_data) 
    for movie in movies_watched_by_friends_list:
        if movie["genre"] == most_frequently_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    '''
    This function determines a list of recommended movies. 
    A movie should be added to this list if it is in the 
    user's "favorites" and none of the user's friends 
    have watched it.
    '''
    recommended_movies = []
    movies_watched_by_friends_dic = get_friends_movies_watched_titles(user_data["friends"])
    for movie in user_data["favorites"]:
        if movie["title"] not in movies_watched_by_friends_dic:
            recommended_movies.append(movie)
    return recommended_movies
