import pytest
# NOTE: In production code, we developers should change import * to something more specific. Due to some constraints of this project, we will import * in our test files.
from viewing_party.main import *


def test_create_movie_all_params_valid_returns_movie():
    # Arrange
    movie_title = "Title A"
    genre = "Horror"
    rating = 3.5

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie["title"] is "Title A"
    assert new_movie["genre"] is "Horror"
    assert new_movie["rating"] is 3.5


def test_create_movie_no_title_returns_none():
    # Arrange
    movie_title = None
    genre = "Horror"
    rating = 3.5

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None


def test_create_movie_no_genre_returns_none():
    # Arrange
    movie_title = "Title A"
    genre = None
    rating = 3.5

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None




def test_create_movie_no_rating_returns_none():
    # Arrange
    movie_title = "Title A"
    genre = "Horror"
    rating = None

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None


def test_add_to_watched_adds_movie_to_user_watched():
    # Arrange
    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    user_data = {
        "watched": []
    }

    # Act
    updated_data = add_to_watched(user_data, movie)

    # Assert
    assert len(updated_data["watched"]) is 1
    assert updated_data["watched"][0]["title"] is "Title A"
    assert updated_data["watched"][0]["genre"] is "Horror"
    assert updated_data["watched"][0]["rating"] is 3.5


def test_add_to_watchlist_adds_movie_to_user_watchlist():
    # Arrange
    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    user_data = {
        "watchlist": []
    }

    # Act
    updated_data = add_to_watchlist(user_data, movie)

    # Assert
    assert len(updated_data["watchlist"]) is 1
    assert updated_data["watchlist"][0]["title"] is "Title A"
    assert updated_data["watchlist"][0]["genre"] is "Horror"
    assert updated_data["watchlist"][0]["rating"] is 3.5


def test_watch_movie_moves_movie_from_watchlist_to_empty_watched():
    # Arrange
    janes_data = {
        "watchlist": [{
            "title": "Title A",
            "genre": "Fantasy",
            "rating": 4.8
        }],
        "watched": []
    }

    # Act
    updated_data = watch_movie(janes_data, "Title A")

    # Assert
    assert len(updated_data["watchlist"]) is 0
    assert len(updated_data["watched"]) is 1
    assert updated_data["watched"][0]["title"] is "Title A"
    assert updated_data["watched"][0]["genre"] is "Fantasy"
    assert updated_data["watched"][0]["rating"] is 4.8


def test_watch_movie_moves_movie_from_watchlist_to_watched():
    # Arrange
    movie_to_watch = {
        "title": "Title A",
        "genre": "Fantasy",
        "rating": 4.8
    }
    janes_data = {
        "watchlist": [
            {
                "title": "Title B",
                "genre": "Action",
                "rating": 2.0
            },
            movie_to_watch
        ],
        "watched": [
            {
                "title": "Title C",
                "genre": "Intrigue",
                "rating": 3.9
            }
        ]
    }

    # Act
    updated_data = watch_movie(janes_data, movie_to_watch["title"])

    # Assert
    assert len(updated_data["watchlist"]) is 1
    assert len(updated_data["watched"]) is 2
    assert movie_to_watch in updated_data["watched"]


def test_watch_movie_does_nothing_if_movie_not_in_watchlist():
    # Arrange
    movie_to_watch = {
        "title": "Title A",
        "genre": "Fantasy",
        "rating": 4.8
    }
    janes_data = {
        "watchlist": [
            {
                "title": "Title B",
                "genre": "Action",
                "rating": 2.0
            }
        ],
        "watched": [
            {
                "title": "Title C",
                "genre": "Intrigue",
                "rating": 3.9
            }
        ]
    }

    # Act
    updated_data = watch_movie(janes_data, "Title A")

    # Assert
    assert len(updated_data["watchlist"]) is 1
    assert len(updated_data["watched"]) is 1
    assert movie_to_watch not in updated_data["watchlist"]
    assert movie_to_watch not in updated_data["watched"]
