def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    found = find_watchlist_movie_position(user_data["watchlist"], title)
    if found > -1:
        watched = user_data["watchlist"].pop(found)
        user_data["watched"].append(watched)

    return user_data


def find_watchlist_movie_position(watchlist, title):
    pos = 0
    for movie in watchlist:
        if movie["title"] == title:
            return pos
        pos += 1

    return -1

def get_watched_avg_rating(user_data):

    if len(user_data["watched"]) == 0:
        return 0

    total = 0
    for movie in user_data["watched"]:
        total += movie["rating"]

    return total / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genres = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        count = genres.get(genre, 0) + 1
        genres[genre] = count

    max_genre = None
    max_count = -1
    for genre, count in genres.items():
        if count > max_count:
            max_genre = genre

    return max_genre

def get_unique_watched(user_data):
    friends_watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched[movie["title"]] = True

    unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    watched = {}
    for movie in user_data["watched"]:
        watched[movie["title"]] = True

    friends_unique = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in watched:
                friends_unique.append(movie)

            watched[movie["title"]] = True

    return friends_unique

def get_available_recs(user_data):
    subs = {}
    for sub in user_data["subscriptions"]:
        subs[sub] = True

    watched = {}
    for movie in user_data["watched"]:
        watched[movie["title"]] = movie

    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            if title in watched:
                continue

            service = movie["host"]
            if service not in subs:
                continue

            recommendations.append(movie)
            watched[title] = movie

    return recommendations

def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    if genre is None:
        return []

    watched = {}
    for movie in user_data["watched"]:
        watched[movie["title"]] = movie

    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            if title in watched:
                continue

            if movie["genre"] == genre:
                continue

            recommendations.append(movie)
            watched[title] = movie

    return recommendations

def get_rec_from_favorites(user_data):
    watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            watched[title] = movie

    recommendations = []
    for fav in user_data.get("favorites", []):
        title = fav["title"]
        if title not in watched:
            recommendations.append(fav)

    return recommendations
