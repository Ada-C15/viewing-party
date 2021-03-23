#Test_wave_1
def create_movie(title, genre, rating):
    """
    checks if three given parameter is true 
    input: For three parameters(title, genre, rating)
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


def add_to_watched(user_data, movie):
    """
    Adds dict to watched 
    input: two parameters(user_data, movie)
    out: updates data 
    """
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """
    Adds dict to watchlist 
    input: two parameters(user_data, movie)
    output: 
    """
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie):
    """
    stores data from "watchlist" to "watched"
    input: two paramemters(user_data, movie)
    output: returns updated data  
    """
    for item in user_data["watchlist"]:
        if movie == item["title"]:

            user_data["watched"].append(item)
            user_data["watchlist"].append(item)
    return user_data

#Test_wave_2
def get_watched_avg_rating(user_data):
    """
    Getting an average of watched movie rating
    input: user_data
    output: average of watched movie rating 
    """
    for movie in user_data["watched"]:
        if user_data["watched"]:
            return(mean["rating"])
        else: 
            return 0 
    


