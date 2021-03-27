def create_movie(movie_title,genre,rating):

    new_movie={
        "title":movie_title,
        "genre":genre,
        "rating":rating
    }

    for values in new_movie.values():
      if values==None:
        return None
      
    return new_movie

def add_to_watched(user_data, movie):
    added_data = user_data["watched"] 
    added_data.append(movie) 
    return user_data
    

def add_to_watchlist(user_data, movie):
    added_data = user_data["watchlist"] 
    added_data.append(movie) 
    return user_data   


def watch_movie(user_data, title):
    user_watchlist_list=user_data["watchlist"]
    
    for dicts in user_watchlist_list:
        
        if dicts["title"]==title:
        
            user_data=add_to_watched(user_data,dicts)
            
            user_data["watchlist"].remove(dicts)
            return user_data
        
    return user_data
       


def get_watched_avg_rating(user_data):
    total_rating=0
    
    user_watched_list=user_data["watched"]
    if user_watched_list==[]:
      return float(0)
    else:
      for item in user_watched_list:
      
        total_rating+=item["rating"]
        average=total_rating/len(user_watched_list)
      return average


def get_most_watched_genre(user_data):
    genre_list=[]
    inner_watch_list=user_data["watched"]
    if inner_watch_list==[]:
      return None
    else:
        for dict in inner_watch_list:
          genre_list.append(dict["genre"])
    
    count_dict={}
    for genre_type in genre_list:
      if genre_type not in count_dict.keys():
        count_dict[genre_type] =1
      else:
        count_dict[genre_type] +=1
    
    return max(count_dict,key=lambda key:count_dict[key])

                 

def get_friends_watched_list(user_data):
  """Creates a list of movies with non repeates for friends category in user_data"""
  friends_watched_list=[]
  boolean_list=[]
  for item in user_data["friends"]:
    if item["watched"]!=[]:
      boolean_list.append("True")
    else:
      boolean_list.append("False")
  for items in boolean_list:
    if items == "False":     
      return friends_watched_list
  
  for item in user_data["friends"]:
    for movie_dict in item["watched"]:
      if movie_dict not in friends_watched_list:

        friends_watched_list.append(movie_dict)
  return friends_watched_list        
          
def get_unique_watched(user_data):
  user_watched_list=user_data["watched"]
  friend_watched_list=get_friends_watched_list(user_data)
  user_unique_watched=[]
  if user_watched_list == []:
    print(user_watched_list)
  else: 
    for movie in user_watched_list:
      if movie not in friend_watched_list:
        user_unique_watched.append(movie)
  return user_unique_watched



def get_friends_unique_watched(user_data):
  user_watched_list=user_data["watched"]
  friend_watched_list=get_friends_watched_list(user_data)
  user_unique_watched=[]
  if friend_watched_list==[]:
    return []
  else:
    for movie in friend_watched_list:
      if movie not in user_watched_list:
        user_unique_watched.append(movie)
  return user_unique_watched


def get_available_recs(user_data):
  user_subs=user_data["subscriptions"]
  friends_movie_list=get_friends_watched_list(user_data)
  final_rec_list=[]
  for movie in friends_movie_list:
    for subs in user_subs:
      if movie["host"]==subs:
        final_rec_list.append(movie)
  return final_rec_list


def get_new_rec_by_genre(user_data):
  user_watched_list=user_data["watched"]
  friend_watched_list=get_friends_watched_list(user_data)
  user_unique_watched=[]
  if user_watched_list == []:
    return []
  else:
    for movie in friend_watched_list:
      if movie not in user_watched_list:
        user_unique_watched.append(movie)
  return user_unique_watched


def get_rec_from_favorites(user_data):
  user_watched_list=user_data["watched"]
  user_favorites_list=user_data["favorites"]
  friends_movie_list=get_friends_watched_list(user_data)
  master_rec_list=[]
  for movies in user_watched_list:
    if movies not in friends_movie_list and movies in user_favorites_list:
      master_rec_list.append(movies)
  return master_rec_list
  