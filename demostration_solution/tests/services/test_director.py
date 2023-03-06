from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture()
def dao_director():
    dao_director = DirectorDAO(None)

    director_1 = Director(id=1, name="Gloria")
    director_2 = Director(id=2, name="Alex")
    director_3 = Director(id=3, name="Marty")
    director_4 = Director(id=4, name="Melman")

    dao_director.get_one = MagicMock(return_value=director_1)
    dao_director.get_all = MagicMock(return_value=[director_1, director_2, director_3, director_4])
    dao_director.create = MagicMock(return_value=Director(id=2))
    dao_director.update = MagicMock()
    dao_director.delete = MagicMock()
    return dao_director

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def service_director(self, dao_director):
        self.service_director = DirectorService(dao_director)

    def test_get_one(self):
        director = self.service_director.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.service_director.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_data ={"name": "Egor"}
        director = self.service_director.create(director_data)
        assert director is not None

    def test_update(self):
        director_data = {"id": 4, "name": "Egor"}
        self.service_director.update(director_data)

    def test_delete(self):
        self.service_director.delete(1)



