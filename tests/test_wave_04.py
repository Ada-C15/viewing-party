import pytest
from viewing_party.main import *

# TEST 19 - WAVE 4 
def test_get_available_recs_returns_appropriate_recommendations_for_valid_input():
    # Arrange
    amandas_data = {
        "subscriptions":["Service A", "Service B"],
        "watched":      [],
        "friends":      [
                        {"watched":[{"title": "Title A",
                                    "host": "Service A"},
                                    {"title": "Title C",
                                    "host": "Service C"}]},
                        {"watched":[{"title": "Title A",
                                    "host": "Service A"},
                                    {"title": "Title B",
                                    "host": "Service B"},
                                    {"title": "Title D",
                                    "host": "Service D"}]}]
                    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) is 2
    assert {"title": "Title A", "host": "Service A"} in recommendations
    assert {"title": "Title B", "host": "Service B"} in recommendations

# TEST 20 - WAVE 4 - PASSED!
def test_get_available_recs_returns_empty_list_for_valid_input_with_no_intersection_in_subscriptions():
    # Arrange
    amandas_data = {
        "subscriptions": ["Service A", "Service B"],
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title C",
                        "host": "Service C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title D",
                        "host": "Service D"
                    }
                ]
            }
        ]
    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) is 0
