from viewing_party.main import *

sonyas_data = {
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


recommendations = get_new_rec_by_genre(sonyas_data)

#print(recommendations)

# testing get most watched genre 
# janes_data = {
#     "watched": [
#         {
#             "title": "Title A",
#             "genre": "Fantasy"
#         },
#         {
#             "title": "Title B",
#             "genre": "Intrigue"
#         },
#         {
#             "title": "Title C",
#             "genre": "Intrigue"
#         },
#         {
#             "title": "Title D",
#             "genre": "Fantasy"
#         },
#         {
#             "title": "Title E",
#             "genre": "Intrigue"
#         },
#     ]
# }
janes_data = {
        "watched": []
    }


genre_dict = calculate_genre_freq(janes_data)


most_watched = get_most_watched_genre(janes_data)
print(most_watched)

# watched = []
# print(bool(watched))
