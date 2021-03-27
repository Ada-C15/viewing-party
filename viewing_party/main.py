from collections import Counter
#import operator

def create_movie(movie_title, genre, rating):
  new_movie = dict()
  new_movie.update([("title", movie_title), ("genre", genre),
    ("rating", rating)])
  for my_key, my_value in new_movie.items():
    if not my_value:
      return None
  else:
    return new_movie

def add_to_watched(user_data, movie):
  user_data = {"watched": []}
  user_data["watched"].append(movie)
  return user_data

def add_to_watchlist(user_data, movie):
  user_data = {"watchlist": []}
  user_data["watchlist"].append(movie)
  return user_data

def watch_movie(user_data, title):
  watchlist_list = user_data["watchlist"]
  watchedlist = user_data["watched"]
  #these are lists of movies not watched, watched
  for movie in watchlist_list:
    #for each element(dict) in list
    for movie_title in movie.values():
      if movie_title == title:

        watchlist_list.remove(movie)
        watchedlist.append(movie)
          
  return user_data 
  
  
def get_watched_avg_rating(user_data):
  #the value of user_data will be a dictionary with a "watched" list of movie dictionaries
  watched_movie_list = user_data['watched']
  rating_list = []
  average = 0
  if len(watched_movie_list) == 0:
    return 0.0
  for movie in watched_movie_list:
    rating_list.append(movie['rating'])
  average = sum(rating_list) / len(rating_list)
  return average

def get_most_watched_genre_dict(user_data):
  genre_dict = {}
  for watched in user_data["watched"]:
    if watched["genre"] not in genre_dict:
      genre_dict[watched["genre"]] = 1
    else:
      genre_dict[watched["genre"]] += 1
  return genre_dict

def get_most_watched_genre(user_data):
  genre_dict = get_most_watched_genre_dict(user_data)
  top_count = 0
  top_key = None
  for genre, genre_count in genre_dict.items():
    if genre_count > top_count:
      top_count = genre_count
      top_key = genre
  return top_key


def get_unique_watched(user_data): 
  my_titles = []
  friends_titles = []
  unique_movies = []
  for movie in user_data["watched"]:
    my_titles.append(movie)
  
  for friend in user_data["friends"]:
    for movie_title in friend["watched"]:
      friends_titles.append(movie_title)
  for movie in user_data["watched"]:
    if movie not in friends_titles:
      unique_movies.append(movie) 
  return unique_movies  

def get_friends_unique_watched(user_data):
  friends_titles = []
  friends_unique_movies = []  
  for friend in user_data["friends"]:
    for movie_title in friend["watched"]:
      friends_titles.append(movie_title)
  for movie in friends_titles:
    if movie not in user_data["watched"]:
      if movie not in friends_unique_movies:
        friends_unique_movies.append(movie)
  
  return friends_unique_movies

def get_available_recs(user_data):
  recd_movies = []
  friends_movie_list = get_friends_unique_watched(user_data)
  subscriptions = user_data['subscriptions']
  for service in subscriptions:
    for movie in friends_movie_list:
      if service in movie['host']:
        recd_movies.append(movie)
  return recd_movies

def get_new_rec_by_genre(user_data):
  recommended_movies = []
  not_watched_movies = []
  top_genre = get_most_watched_genre(user_data)
  for friend in user_data['friends']:
    for movie in friend["watched"]:
      if movie not in user_data["watched"]:
        not_watched_movies.append(movie)
  for movie in not_watched_movies:
    for value in movie.values():
      if top_genre == value:
        recommended_movies.append(movie)
        
  return recommended_movies

def get_rec_from_favorites(user_data):
  recommended_movies = []
  friends_movie_list = []
 # friends_movie_list = get_friends_unique_watched(user_data)

  for friend in user_data['friends']:
    for movie in friend["watched"]:
      friends_movie_list.append(movie)

  for movie in user_data["favorites"]:
    if movie not in friends_movie_list:
      recommended_movies.append(movie)
    
  return recommended_movies

