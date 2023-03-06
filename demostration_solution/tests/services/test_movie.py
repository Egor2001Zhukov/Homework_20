from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.director import DirectorService
from demostration_solution.service.movie import MovieService


@pytest.fixture()
def dao_movie():
    dao_movie = MovieDAO(None)

    movie_1 = Movie(id=1, title="Gloria")
    movie_2 = Movie(id=2, title="Alex")
    movie_3 = Movie(id=3, title="Marty")


    dao_movie.get_one = MagicMock(return_value=movie_1)
    dao_movie.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    dao_movie.create = MagicMock(return_value=Movie(id=2))
    dao_movie.update = MagicMock()
    dao_movie.delete = MagicMock()
    return dao_movie

class TestMovieService:
    @pytest.fixture(autouse=True)
    def service_movie(self, dao_movie):
        self.service_movie = MovieService(dao_movie)

    def test_get_one(self):
        movie = self.service_movie.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.service_movie.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_data ={"name": "Egor"}
        movie = self.service_movie.create(movie_data)
        assert movie is not None

    def test_update(self):
        movie_data = {"id": 4, "name": "Egor"}
        self.service_movie.update(movie_data)

    def test_delete(self):
        self.service_movie.delete(1)



