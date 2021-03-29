from main import *
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

# Act
recommendations = get_new_rec_by_genre(sonyas_data)
print(recommendations)