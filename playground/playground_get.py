user_data = {
    "subscription": ["Service A", "Service B"],
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

user_friends_matched_subscr = []
for subscr in user_data.get("subscriptions", ["a", "b"]):
    print(subscr)
    # for friend in user_data.get(["friends"], []):
    #     for friend_list in friend.values():
    #         for movie in friend_list:
    #             if movie["host"] == subscr:
    #                 if (movie not in user_data["watched"]) and (
    #                         movie not in user_friends_matched_subscr):
    #                     user_friends_matched_subscr.append(movie)

print(user_friends_matched_subscr)
