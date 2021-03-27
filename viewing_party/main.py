
# create movie function

def create_movie(title, genre, rating):
    new_movie = {
        "title": title,
        "genre": genre, 
        "rating": rating 
    }
    if title and genre and rating:
        return new_movie
    else:
        return None
    
#adds movie to user watched
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
#adds movie to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#moves movie from watchlist to empty watched list   
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            add_to_watched(user_data, movie)
    return user_data
#Calculate the average rating of all movies in watched list
#return the average rating
def get_watched_avg_rating(user_data):
    if user_data["watched"]:  
        count = 0
        for movie in user_data["watched"]:
            count += movie["rating"]
            average = count / len(user_data["watched"])
        return average
    else: 
        return 0.0
    
#finds the most watched genre
def get_most_watched_genre(user_data):
    most_watched_dict = {} 
    popular_genre = None
    for movie in user_data["watched"]:
        if movie["genre"] not in most_watched_dict:
            most_watched_dict[movie["genre"]] = 1
        else: 
             most_watched_dict[movie["genre"]] += 1
        popular_genre = max(most_watched_dict, key = most_watched_dict.get)
        
    return popular_genre

# compares list1 to list2 and returns unique info from list1
def get_unique(list1, list2):
    unique_list = []
    for list_element in list1:
        is_unique = True
        for list_item in list2:
            if list_element['title'].lower() == list_item['title'].lower():
                is_unique = False
                break

        if is_unique:
            unique_list.append(list_element)
    
    return unique_list
#returns list of movies in the users data absent from their friends data
def get_unique_watched(user_data):
    user_titles_list = []
    friends_list = []
    for movie in user_data["watched"]:
        user_titles_list.append(movie)
    for friend in user_data["friends"]:
        for friend_movie_watched in friend["watched"]:
            friends_list.append(friend_movie_watched) 
    for movie in friends_list:
        if movie in user_titles_list:
            user_titles_list.remove(movie)
    return user_titles_list
#returns list of movies the user has not watched and friends have but does not include two of the same movie
def get_friends_unique_watched(user_data):
    user_watched_movies = []
    friends_watched_movies = []
    for movie in user_data["watched"]:
        user_watched_movies.append(movie)
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in friends_watched_movies:
                friends_watched_movies.append(friend_movie)
    friends_unique_list = get_unique(friends_watched_movies, user_watched_movies)
    return friends_unique_list



# userdata = {"watched": [
#                 {"title": "Cars", "host": "Hulu"},
#                 {"title": "Cars", "host": "Hulu"},
#     ], 
#     "friends" :  [
#     {
#         "watched": [
#             {"title": "Cars", "host": "Hulu"},
#             {"title": "She", "host": "Netflix"}
#         ]
#     },
#     {
#         "watched": [
#             {"title": "Inn", "host": "Amazon Prime", "genre": "Drama"},
#             {"title": "Out", "host": "Disney Plus", "genre": "Drama"},
#             {"title": "Outlander", "host": "Netflix", "genre": "Romance"}
#         ]
#     }
# ]




def get_available_recs(user_data):
    subscription = user_data["subscriptions"]
    user_watched_movies = user_data["watched"]
    recommended_movie_list = []
    friends_watched_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
                 friends_watched_movies.append(movie)
    for movie in friends_watched_movies:
        if movie["title"] not in user_watched_movies and movie not in recommended_movie_list:
            if movie["host"] in subscription:
                 recommended_movie_list.append(movie)
        
    return recommended_movie_list

# Wave 5

"""
There are four tests about a get_new_rec_by_genre function
Create a function named get_new_rec_by_genre
takes one parameter: user_data

Consider the user's most frequently watched genre. 
Then, determine a list of recommended movies.

A movie should be added to this list if and only if:
The user has not watched it
At least one of the user's friends has watched

The "genre" of the movie is the same as the user's most frequent genre
Return the list of recommended movies
There is also one test about a get_rec_from_favorites function
"""

# fav_genre = "romanCE"
# fav_genre.lower() # romance

# friends_watched = [
#     {"title": "Harry Potter", "genre":"Magical fiction"},
#     {"title": "Hulk", "genre":"Action"},
#     {"title": "Call me by your name", "genre":"Romance"}
# ]


def get_new_rec_by_genre(user_data):
    recommendations = []
    # if watched list has some data, only then do the next steps
    if user_data["watched"]:
        # get the most watched genre by calling get_most_watched_genre function
        most_frequent_genre = get_most_watched_genre(user_data)
        # get movies uniques to friends so that it can be recommended to user 
        friends_unique_watched = get_friends_unique_watched(user_data)
        # filter out all the movies that belong to the genre that the user likes the most, and return it
        if friends_unique_watched:
            for movie in friends_unique_watched:
                if movie["genre"].lower() == most_frequent_genre.lower():
                    recommendations.append(movie)

    return recommendations
            
"""
Create a function named get_rec_from_favorites
takes one parameter: user_data

user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
This represents the user's favorite movies

Consider the user's most frequently watched genre. 

Then, determine a list of recommended movies. A movie should be added to this list if and only if:

The movie is in the user's "favorites"
None of the user's friends have watched it

Return the list of recommended movies
"""
user_data = {
    "favorites" : [
        {"title": "Very very romantic", "genre":"Romance"},
        {"title": "Very Romantic", "genre":"Romance"},
        {"title": "Call me by your name", "genre":"Romance"}
    ]
}

# get movies that are in user's favourites but haven't been watched by friends
def get_rec_from_favorites(user_data):
   
   # 1. compare user's favourites with the movies that friends have watched
   # 2. If friends haven't watched a movie that's in user's favourites
   # 3. append those movies to favourite_recs list
   # 4. return list

    favorite_recs = []
    
    if user_data["favorites"]:
        users_favorites = []
        friends_watched_movies = []

        # get users favorites
        for movie in user_data["favorites"]:
            users_favorites.append(movie)

        #get all the movies watched by friends
        for friend in user_data["friends"]:
            for friend_movie in friend["watched"]:
                if friend_movie not in friends_watched_movies:
                    friends_watched_movies.append(friend_movie)

        favorite_recs = get_unique(users_favorites, friends_watched_movies)

    return favorite_recs
   

   
   
   
   
   
   
   
   
   
 


    
    







  
         

         

        


     
              
    
    
    
    
    


