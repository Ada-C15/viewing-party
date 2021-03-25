
user_data = {
    "watched": [
        {
            "title": "Title A"
        },
        {
            "title": "Title B"
        },
        {
            "title": "Title C"
        }
    ],
    "favorites": [
        {
            "title": "Title A"
        },
        {
            "title": "Title B"
        }
    ],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title B"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title C"
                },
                {
                    "title": "Title D"
                }
            ]
        }
    ]
}


# set([{"title": "Title C"}, {"title": "Title D"}])
# # print(set([{"title": "Title C"}, {"title": "Title D"}]))

# print(user_data["favorites"])

# print(set(user_data["watched"]["title"]).intersection(
#     set(user_data["favorites"][["title"]])))

# list_1 = [{'title': 'Title A'}, {'title': 'Title B'}, {'title': 'Title C'}]
# list2 = [{'title': 'Title A'}, {'title': 'Title B'}]


# result_list = []
# for movie in user_data["favorites"]:
#     print(movie)
#     for friend in user_data["friends"]:
#         print(friend)
#         for movie_name in friend["watched"]:
#             print("comparson:")
#             print(movie_name)
#             print(movie["title"])
#             print(movie_name["title"])
#             if movie["title"] != movie_name["title"] and movie["title"] not in result_list:
#                 result_list.append(movie["title"])

# print(result_list)
friends_watched_titles = []
for friend in user_data["friends"]:
    for friend_list in friend.values():
        for movie in friend_list:
            friends_watched_titles.append(movie["title"])
friends_watched_titles = list(set(friends_watched_titles))

user_fav_titles = []
for movie in user_data["favorites"]:
    user_fav_titles.append(movie["title"])
user_fav_titles = list(set(user_fav_titles))

result = [movie for movie in user_fav_titles if movie not in friends_watched_titles]
