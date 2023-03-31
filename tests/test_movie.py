from viewing_party.movie import Movie
import pytest

def test_movie_class_initializes_with_all_attribute():
    # Arrange/ Act
    movie1 = Movie("Goonies", "fun", 5)
    
    # Assert
    assert movie1.name == "Goonies"
    assert movie1.genre == "fun"
    assert movie1.rating == 5