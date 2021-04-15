user_data = {
    "watched": [
        {
            "title": "Title A",
            "genre": "Intrigue"
        },
        {
            "title": "Title B",
            "genre": "Intrigue"
        },
        {
            "title": "Title C",
            "genre": "Fantasy"
        }
    ],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title D",
                    "genre": "Intrigue"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title C",
                    "genre": "Fantasy"
                },
                {
                    "title": "Title E",
                    "genre": "Intrigue"
                }
            ]
        }
    ]
}


def get_most_watched_genre(user_data):
    """
    Returns the genre from the user list of "watched" movies,
    that is the most frequently watched
    user_data = {"watched": [movie1, movie2, movie3]}
    movie = {"genre": "string"}
    """
    if len(user_data["watched"]) > 0:
        genre_dict = {}  # this dictionary will hold info regarding frequency
        for movie in user_data["watched"]:
            if movie["genre"] in genre_dict.keys():
                genre_dict[movie["genre"]] += 1
            else:
                genre_dict[movie["genre"]] = 1
    else:
        return None

    max_genre_rating = max(genre_dict.values())
    position = list(genre_dict.values()).index(max_genre_rating)
    return list(genre_dict.keys())[position]


def get_friends_unique_watched(user_data):
    """
    Creates a list of dictionaries, that represents a list of movies
    that at least one of the user's friends have watched, but the user has not watched.

    user_data = {
        "watched": [{"title": "Title A"}, {"title": "Title B"}, {"title": "Title C"}],
        "friends": [{"watched": [{"title": "Title A"},{"title": "Title B"}]}, {}, {}]
        }
    """

    user_watched_titles = []
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])
    user_watched_titles = list(set(user_watched_titles))

    friends_watched_titles = []
    for friend in user_data["friends"]:
        for friend_list in friend.values():
            for movie in friend_list:
                friends_watched_titles.append(movie["title"])
    friends_watched_titles = list(set(friends_watched_titles))

    friends_unique_watched_list = []
    for title in friends_watched_titles:
        if title not in user_watched_titles:
            friends_unique_watched_list.append({"title": title})

    return friends_unique_watched_list


def get_new_rec_by_genre(user_data):
    """
    """

    # Consider the user's most frequently watched genre.
    user_most_watched_genre = get_most_watched_genre(user_data)
    # print(user_most_watched_genre)

    # Determine a list of recommended movies.
    rec_movies_list = get_friends_unique_watched(user_data)
    # print(rec_movies_list)

    # resulting_list = []
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if movie["genre"] == user_most_watched_genre:
    #             resulting_list.append(movie)

    resulting_list = [movie for friend in user_data["friends"]
                      for movie in friend["watched"] if movie["genre"] == user_most_watched_genre]
                      
    return resulting_list


print(get_new_rec_by_genre(user_data))
