from viewing_party.person import Person
from viewing_party.movie import Movie

import pytest

def test_creating_person_initializes_instance_variables():
    # Arrange / Act
    kendall = Person("Kendall")

    # Assert
    assert kendall.name == "Kendall"
    assert kendall.friends == []

def test_adding_friend_multiple_times_does_not_create_duplicate():
    # Arrange
    kendall = Person("Kendall")
    simon = Person("Simon")

    # Act
    kendall.add_friend(simon)
    kendall.add_friend(simon)

    # Assert
    assert kendall.friends == [simon]

def test_add_movie_to_watchlist_returns_watchlist_with_correct_movies():
    # Arrange
    kendall = Person("Kendall")
    movie1 = Movie("Goonies", "fun", 5)
    movie2 = Movie("Freaky Friday", "teen flick", 4)

    # Act
    kendall.add_movie_to_watchlist(movie1)
    kendall.add_movie_to_watchlist(movie2)
    kendall.add_movie_to_watchlist(movie1)

    # Assert
    assert kendall.watchlist[0] == movie1
    assert kendall.watchlist[1] == movie2
    assert len(kendall.watchlist) == 2