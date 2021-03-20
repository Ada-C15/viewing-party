def create_movie(title, genre, rating):

    #updated_data= {}
    #movie_to_watch = {}
   
    if (title) and (genre) and (rating):
        new_movie = {"title" : title, "genre" : genre,  "rating" : rating } 
        return new_movie
        
    elif (not title) or (not genre) or (not rating):
        return None

    else:
        return None
    
def add_to_watched(user_data, new_movie):

    #user_data = {"watched": []}

    user_data["watched"].append(new_movie)

    return user_data

def add_to_watchlist(user_data, movie):

    #user_data = { "watchlist": []}

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    #user_data = { "watchlist": [],
                  # "watched" : []}
    for watchlist_movie in user_data["watchlist"]:
        if title == watchlist_movie["title"]:
            user_data["watchlist"].remove(watchlist_movie)
            user_data["watched"].append(watchlist_movie)
            return user_data  #breaking because it has found the movie and it does not need to iterate over the list.
        
    return user_data

# WAVE 2

def get_watched_avg_rating(user_data):

    sum_of_ratings = 0
    average_rating = 0
    watched_list = user_data["watched"]

    if(len(watched_list) == 0):
        return 0.0

    for watched_movie in watched_list:

        sum_of_ratings = sum_of_ratings + watched_movie["rating"]

    list_length = len(watched_list)
    average_rating = sum_of_ratings / list_length

    return (float(average_rating))


def get_most_watched_genre(user_data):

    watched_list = user_data["watched"]

    # Create dict genre_counts with key as genre name and value as frequency of that genre

    # Iterate over the watched movie list and populate the genre_counts dict

    # find the nax value of the genre_counts.values() ==> max frequency

    # Find the genre name that corresponds to the max frequency count

    # return genre_name
            



# test program starts here
new_movie1 = create_movie("m1", "ab", 3)
new_movie2 = create_movie("m2", "ac", 4)
new_movie3 = create_movie("m3", "ad", 2)
new_movie4 = create_movie("m4", "aef", 1)

user_data = { "watchlist": [new_movie1, new_movie2, new_movie3, new_movie4],
            "watched" : [new_movie1, new_movie2, new_movie3, new_movie4]}
    
get_most_watched_genre(user_data)