def create_movie(title, genre, rating):
      # if all three parameters are truthy, return a dict with key val pairs
       #return a dictionary with 3 keys title, genre, rating 
    #else title, genre, or rating is falsey
        #return None
    movie_dict = {}
    movie_args = []
    movie_args.append(title)
    movie_args.append(genre)
    movie_args.append(rating)
    for i in movie_args:
        if not i:
            return None
            
    
    movie_dict['title'] = movie_args[0]
    movie_dict['genre'] = movie_args[1]
    movie_dict['rating'] = movie_args[2]
    return movie_dict
   

def add_to_watched(user_data, movie):
    # user_data = {'watched':[]} empty list means no watched movies in their watched[]
   
    user_data['watched'].append(movie)
    return user_data
   
def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    
    return user_data

def watch_movie(user_data, title):
    
    for movie in user_data['watchlist']:
        if title == movie['title']:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
        
    return user_data

def get_watched_avg_rating(user_data):
    rating_sum = 0
    count = 0
    avg_rating = 0
    
    if user_data['watched'] == []:
        return avg_rating
    for movie in user_data['watched']:
        rating_sum += movie['rating']
        count += 1
    avg_rating = rating_sum/count 
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list = []
    for key in user_data['watched']:
        genre_list.append(key['genre'])
    genre_dict = {}

    for genre in genre_list:
        if genre in genre_dict:
            genre_dict[genre] = genre_dict[genre] + 1 
        else:
            genre_dict[genre] = 1
    genre_count_list = []
    for key, val in genre_dict.items():
        genre_count_list.append(val)
    genre_count_list.sort()
    for key, val in genre_dict.items():
        if val == genre_count_list[-1]:
            return key 

def get_unique_watched(user_data):
    user_watched_set = set()
    for movie in user_data['watched']:
        user_watched_set.add(movie['title'])
    
    friend_watched_set = set()
    for movie in user_data['friends']:
        for val in movie['watched']:
            friend_watched_set.add(val['title'])
            
    user_watched_not_friend_watched = user_watched_set.difference(friend_watched_set)
    
    movie_dict_list = []
    movie_dict = {}
    for i in user_watched_not_friend_watched:
        movie_dict_list.append({'title':i})
    
    return movie_dict_list

def get_friends_unique_watched(user_data):
    user_watched_set = set()
    for movie in user_data['watched']:
        user_watched_set.add(movie['title'])
    
    friend_watched_set = set()
    for movie in user_data['friends']:
        for val in movie['watched']:
            friend_watched_set.add(val['title'])
    
    friend_watched_not_user_watched = friend_watched_set.difference(user_watched_set)
    
    movie_dict_list = []
    movie_dict= {}
    for i in friend_watched_not_user_watched:
        movie_dict_list.append({'title':i})
    return movie_dict_list

def get_available_recs(user_data):
  
    user_hosts = user_data['subscriptions']
    user_watched = user_data['watched']
    friends_watched = user_data['friends']
    recommendations = []
    
    for movie_dict in friends_watched:
        #print(movie_dict)
        for movie in movie_dict['watched']:
            print(movie,"HERE")
            #for key,val in movie.items():
                #print(key,val)
                #print(movie_dict['title'])
            if movie['host'] in user_data['subscriptions']:
                if movie['title'] not in user_watched:
                        if movie not in recommendations:
                            recommendations.append(movie)
    return recommendations


def get_new_rec_by_genre(user_data):
       
    recommendations = []
    user_watched = user_data['watched']
    
    if len(user_watched) == 0:
        return []
    user_most_watched_genre = get_most_watched_genre(user_data)
    #print(user_last_watched_genre,'most watched genre')
    friends = user_data['friends']
    for friend in friends:
        #print(friend)
        for movie in friend['watched']:
            #print(movie['genre'],'movie')
            
            if movie['genre'] == user_most_watched_genre:
                if movie not in recommendations:
                    recommendations.append(movie) 
    return recommendations

def get_rec_from_favorites(user_data):
    friends_watched_movies = set()
    recs = []
    for friend in user_data["friends"]: 
        for movie in friend["watched"]: 
            friends_watched_movies.add(movie["title"])
            print(f"friends set {friends_watched_movies}")
    #breakpoint()
    #list of users favorites 
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_watched_movies: 
            recs.append(movie)
            print(recs)
    return recs