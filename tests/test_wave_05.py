
import pytest
from viewing_party.main import *


def test_get_new_rec_by_genre_returns_appropriate_recommendations_for_large_amount_of_valid_input():
    # Arrange
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

    # Assert
    for rec in recommendations:
        assert rec not in sonyas_data["watched"]
    assert len(recommendations) is 2
    assert {"title": "Title D", "genre": "Intrigue"} in recommendations
    assert {"title": "Title E", "genre": "Intrigue"} in recommendations


def test_get_new_rec_by_genre_returns_empty_list_when_sonyas_watched_list_is_empty():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "genre": "Intrigue"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title B",
                        "genre": "Fantasy"
                    },
                    {
                        "title": "Title C",
                        "genre": "Intrigue"
                    }
                ]
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) is 0


def test_get_new_rec_by_genre_returns_empty_list_when_friends_watched_lists_are_empty():
    # Arrange
    sonyas_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Intrigue"
            }
        ],
        "friends": [
            {
                "watched": []
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) is 0



def test_get_new_rec_by_genre_returns_empty_list_when_sonya_has_no_favories_and_no_unique_movie_in_watched_list():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "genre": "Intrigue"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title B",
                        "genre": "Fantasy"
                    },
                    {
                        "title": "Title C",
                        "genre": "Intrigue"
                    }
                ]
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) is 0


def test_get_rec_from_favorites_returns_expected_list_from_valid_input():
    # Arrange
    sonyas_data = {
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

    # Act
    recommendations = get_rec_from_favorites(sonyas_data)

    # Assert
    assert len(recommendations) is 1
    assert {"title": "Title A"} in recommendations
