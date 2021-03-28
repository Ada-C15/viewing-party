# wave 1
def create_movie(movie_title, genre, rating):
    new_movie = {}
    if movie_title == None or genre == None or rating == None:
        new_movie = None
    else:
        new_movie["title"] = movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data = {
        "watched":[
            movie
        ]
        }
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist":[
            movie
        ]
        }
    return user_data

def watch_movie(user_data,title):
    for movie in user_data['watchlist']:
        if title == movie['title']:
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
            return user_data
    return user_data

# Wave 2

def get_watched_avg_rating(user_data):
    value = []
    for movie in user_data["watched"]:
        rating_num = movie['rating']
        value.append(rating_num)
    total = sum(value)
    if total != 0:
        average = total/len(value)
    else:
        average = 0.0
    return average

def get_most_watched_genre(user_data):
    genre_list = []
    if len(user_data['watched']) == 0:
        popular_genre = None
        return popular_genre
    for movie in user_data['watched']:
        genre = movie['genre']
        genre_list.append(genre)
        popular_genre = max(set(genre_list), key = genre_list.count)
    return popular_genre

# Wave 3

def get_friend_titles(user_data):
    friends = user_data["friends"]
    friends_titles = []
    for watched_movies in friends:
        for movie in watched_movies["watched"]:
            friends_titles.append(movie)
    return friends_titles

def get_user_titles(user_data):
    user_titles = []
    for movie in user_data["watched"]:
        user_titles.append(movie)
    return user_titles

def get_unique_watched(user_data):
    friends_titles = get_friend_titles(user_data)
    user_titles = get_user_titles(user_data)
    user_unique_titles = []
    for title in user_titles:
        if title not in friends_titles:
            user_unique_titles.append(title)
    return user_unique_titles

def remove_duplicates(titles):
    new_friends_titles = []
    for i in range(len(titles)-1):
        if titles[i] != titles[i+1:]:
            new_friends_titles.append(titles[i+1])
    return new_friends_titles

def get_friends_unique_watched(user_data):
    user_titles = get_user_titles(user_data)
    friends_unique_titles = []
    new_friends_titles = remove_duplicates(get_friend_titles(user_data))
    for title in new_friends_titles:
        if title not in user_titles:
            friends_unique_titles.append(title)
    return friends_unique_titles

# Wave 4
def get_available_recs(user_data):
    friend_data = get_friend_titles(user_data)
    recommendations = []
    friend_data = remove_duplicates(friend_data)
    for data in friend_data:
        if data['host'] in user_data["subscriptions"]:
            recommendations.append(data)
    return recommendations

# Wave 5
def get_new_rec_by_genre(user_data):
    user_titles = get_user_titles(user_data)
    friends_titles = get_friend_titles(user_data)
    recommendations = []
    if user_titles == []:
        recommendations = []
    else:
        for title in friends_titles:
            if title not in user_titles:
                recommendations.append(title)
    return recommendations

def get_rec_from_favorites(user_data):
    user_titles = get_user_titles(user_data)
    friends_titles = get_friend_titles(user_data)
    for movie in friends_titles:
        if movie in user_titles:
            user_titles.remove(movie)
    if user_titles in user_data["favorites"]:
        return user_titles
    return user_titles


