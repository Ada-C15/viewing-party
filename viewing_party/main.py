
#### VIEWING PARTY PROJECT ##### 
#  *****wave 1 testing - tests # 1 - 9 ******
#  test 1 funct that takes in 3 args /creates a dict of movie info 
#  test 2 if title returns none function returns none 
#  test 3 if genre returns none function returns none 
#  test 4 if rating returns none function returns none 
def create_movie(movie_title, genre, rating):
    movie = { 
        'title' : movie_title, 
        'genre': genre, 
        'rating': rating
        }
    if movie['title'] == None or movie['genre'] == None  or movie['rating'] == None: 
        return None
    else: 
        return movie 

#  test 5 funct to add movie to "watched" list, takes in 
# user data (list of dict) and a movie dict returns new list
def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

# test 6 func to add movie to watchlist, takes in user data (list of dict)
#  and a movie dict and returns the new list 
def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

# test 7 func for watched movies moves a movie 
# (by title) from watchlist to empty watched list

# test 8 moves a movie from watched list to watchlist when watchlist is truthy

# test 9 function does nothing if movie title is not in watched list 
def watch_movie(user_data, title):
    for movie_dict in user_data['watchlist']:
        if title in movie_dict.values():
            user_data['watchlist'].remove(movie_dict)
            user_data['watched'].append(movie_dict)
            return user_data
    return user_data  

# *****wave 2 testing test 10 - 13 ***** 
# test 10 funct for avg rating that takes in user_data returns avg of ratings 

# # test 11 function returns 0.0 if no movies in watched list
def get_watched_avg_rating(user_data): 
    if len(user_data['watched']) == 0:
        mean = 0.0
    else:
        ratings = [movie['rating'] for movie in user_data['watched']]       
        mean = sum(ratings) / len(ratings)
    return mean 


# test 12 funct collects the genre data and returns most watched genre 

# test 13 make sure the function returns none if list is empty 
def get_most_watched_genre(user_data):
    word_count = {}
    if user_data['watched'] == []:
        return None
    else:
        for movie_dict in user_data['watched']:
            if movie_dict['genre'] not in word_count:
                word_count[movie_dict['genre']] = 1
            else:
                word_count[movie_dict['genre']] += 1
        max_genre = max(word_count)
        return max_genre



#   ***** wave 3 tests 14-18 **** 
# test 14 funct get_unique_watched takes in user data 
# returns list of movies in user data that are not in friends data

# test 15 returns an empty list if everyone watched the same movies 

def get_unique_watched(user_data):

    friends_watched = []
    for dictionary in user_data['friends']:
        for title_list in dictionary.values():
            for dict in title_list:
                friends_watched.append(dict)


    unique_watched = [movie for movie in user_data['watched']\
         if movie not in friends_watched]

    # for movie_title_dict in user_data['watched']:
    #     if movie_title_dict not in friends_watched:
    #         unique_watched.append(movie_title_dict)

    return unique_watched





# test 16 function get_friends_unique_watched
# takes in user_data determines which movies at least one of 
# users friend has watched, but user has not.  return as 
# list of dict. 

# test 17 does it work with only one friend


#  test 18 make sure the function returns [] if the user has 
# watched all the movies friends have watched. 


def get_friends_unique_watched(user_data): 
    friends_watched = []
# creates a list of dict of movies friends have watched 
    for friend_dict in user_data['friends']:
        for title_list in friend_dict.values():
            for title in title_list:
                friends_watched.append(title)
# set a new list to remove duplicate movies 
    friends_watched_remove_dupes = []
    for movie in friends_watched:
        if movie not in friends_watched_remove_dupes:
            friends_watched_remove_dupes.append(movie)

    more_unique = [movie for movie in friends_watched_remove_dupes 
if movie not in user_data['watched']]

    return more_unique


# ****** wave 4 tests 19 - 20 ******** 
# test 19 funct get_available_recs takes in user_data 
# w/ dict key "subscriptions" value is list strings 
# each friends watched movie data will also have a host key, whose 
# value will be the streaming service as string 
# output should be a list of reccomended moves that 
#   a: user has not watched 
#   b: at least one friend has watched 
#   c: the host of the movie is in the users "subscriptions"

# test 20 ensure you return an empty list if there are no intersections 
def get_available_recs(user_data):
    friends_movies = get_friends_unique_watched(user_data)
    reccomendations = [dictionary for dictionary in 
    friends_movies if dictionary['host'] in 
    user_data['subscriptions']]
    return reccomendations


# ****** test wave 5 tests 20 - 25 ****** 
# test 21 funct get_new_rec_by_genre takes in user_data
# consider most frequently watched genre/determine 
# a list of recco movies - only if: 
#       a. user has not watched it 
#       b. at least one of friends has watched it 
#       c. the genre of the movie is the same as the most freq genre 
# return list of reccomended movies 
# return a valid list with large input
# 
#  
# test 22 return empty list when user_data is empty 

# test 23 return empty list when friends watched lists are empty

# test 24 return empty list when user has no faves and no unique 
# movies in watch list 


def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)
    friends_watched_user_has_not = get_friends_unique_watched(user_data)
    new_rec_by_genre = [movie for movie in friends_watched_user_has_not if
    movie['genre']== most_watched_genre]
    return new_rec_by_genre
    

# test 25 funct get_rec_from_favorites
# take in user_data 
# consider most freq watched genre, then determine a list 
# of recco movies that should be added to the list only if in users 
# favorites and if none of the friends have watched. 

def get_rec_from_favorites(user_data):
    fave_movies = [movie for movie in user_data['favorites']]
    unique_watched = get_unique_watched(user_data)
    recommended_from_faves = [movie for movie in fave_movies if 
    movie in unique_watched]
    return recommended_from_faves


