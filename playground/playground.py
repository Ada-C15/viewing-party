movie = {
    "title": "Title A",
    "genre": "Horror",
    "rating": 3.5
}
amandas_data = {
    "watched": []
}

genre_dict = {
    "Horor": 4,
    "Drama": 3,
    "Triller": 1
}

amandas_data = {
    "subscriptions": ["Service S", "Service Sa"],
    "watched": [],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title C",
                    "host": "Service C"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title B",
                    "host": "Service B"
                },
                {
                    "title": "Title D",
                    "host": "Service D"
                }
            ]
        }
    ]
}

# amandas_data = {
#     "watched": [
#         {
#             "title": "Title B"
#         },
#         {
#             "title": "Title C"
#         }
#     ],
#     "friends": [
#         {
#             "watched": [
#                 {
#                     "title": "Title A"
#                 },
#                 {
#                     "title": "Title C"
#                 }
#             ]
#         },
#         {
#             "watched": [
#                 {
#                     "title": "Title A"
#                 },
#                 {
#                     "title": "Title D"
#                 },
#                 {
#                     "title": "Title E"
#                 }
#             ]
#         }
#     ]
# }

user_friends_matched_subscr = []
print(amandas_data["subscriptions"])
for subscr in amandas_data["subscriptions"]:
    for friend in amandas_data["friends"]:
        for friend_list in friend.values():
            for movie in friend_list:
                if movie["host"] == subscr:
                    if movie not in user_friends_matched_subscr:
                        user_friends_matched_subscr.append(movie)
print(user_friends_matched_subscr)


# friends_watched_hosts = []
# for friend in amandas_data["friends"]:
#     for friend_list in friend.values():
#         for movie in friend_list:
#             friends_watched_hosts.append(movie["host"])
# friends_watched_hosts = list(set(friends_watched_hosts))

# print("Friends has already watched: ")
# print(friends_watched_hosts)
# print()


# user_watched_titles = []
# for movie in amandas_data["watched"]:
#     user_watched_titles.append(movie["title"])
# user_watched_titles = list(set(user_watched_titles))
# print("User has already watched: ")
# print(user_watched_titles)
# print()


# friends_unique_watched_list = []
# for title in friends_watched_titles:
#     if title not in user_watched_titles:
#         friends_unique_watched_list.append({"title": title})
# print("List of Unique Title firends have watched: ")
# print(friends_unique_watched_list)
# print()


# user_watched_titles = []
# for movie in amandas_data["watched"]:
#     if movie["title"] not in friends_watched_titles:
#         user_watched_titles.append(movie["title"])
# user_watched_titles = list(set(user_watched_titles))
# print("These movies are unique for user: ")
# print(user_watched_titles)
# print()

# friends_unique_watched_list = []
# for title in user_watched_titles:
#     friends_unique_watched_list.append({"title": title})
# print(friends_unique_watched_list)

# friends_watched_titles = []
# for friend in amandas_data["friends"]:
#     for friend_list in friend.values():
#         for movie in friend_list:
#             friends_watched_titles.append(movie["title"])
# friends_watched_titles = list(set(friends_watched_titles))


# print("Friends has already watched: ")
# print(friends_watched_titles)
# print()

# user_unique_watched_titles = []
# for movie in amandas_data["watched"]:
#     if movie["title"] not in friends_watched_titles:
#         user_unique_watched_titles.append(movie["title"])
# user_unique_watched_titles = list(set(user_unique_watched_titles))

# print("These movies are unique: ")
# print(user_unique_watched_titles)
# print()

# user_unique_watched_list = []
# for title in user_unique_watched_titles:
#     user_unique_watched_list.append({"title": title})
# print("This is a list of dict of unique movies: ")
# print(user_unique_watched_list)
# print()

# for element in (amandas_data["friends"]):
#     for sub_elem in element.values():
#         for sub_sub_elem in sub_elem:
#             print(sub_sub_elem["title"])

# def add_to_watched(user_data, movie):
#     """
#     adds a movie to the users data/watched list
#     """
#     print("**********************************")
#     print(user_data)
#     print(movie)
#     user_data["watched"].append(movie)
#     return user_data


# # updated = add_to_watched(user_data, movie)
# # print(len(updated))
# # print(updated)

# max_genre_rating = max(genre_dict.values())
# print(max_genre_rating)
