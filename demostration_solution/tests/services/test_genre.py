from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService


@pytest.fixture()
def dao_genre():
    dao_genre = GenreDAO(None)

    genre_1 = Genre(id=1, name="Comedy")
    genre_2 = Genre(id=2, name="Drama")
    genre_3 = Genre(id=3, name="Horor")

    dao_genre.get_one = MagicMock(return_value=genre_1)
    dao_genre.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    dao_genre.create = MagicMock(return_value=Genre(id=2))
    dao_genre.update = MagicMock()
    dao_genre.delete = MagicMock()
    return dao_genre

class TestGenreService:
    @pytest.fixture(autouse=True)
    def service_genre(self, dao_genre):
        self.service_genre = GenreService(dao_genre)

    def test_get_one(self):
        genre = self.service_genre.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.service_genre.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_data ={"name": "Egor"}
        genre = self.service_genre.create(genre_data)
        assert genre is not None

    def test_update(self):
        genre_data = {"id": 4, "name": "Egor"}
        self.service_genre.update(genre_data)

    def test_delete(self):
        self.service_genre.delete(1)



