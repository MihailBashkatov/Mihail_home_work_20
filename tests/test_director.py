import pytest

from service.director import DirectorService

class TestdirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(5)
        assert director is not None
        assert director.id is not None
        assert director.name == 'Иванов'

    def test_get_all(self):
        director = self.director_service.get_all()
        assert director is not None
        assert type(director) == list
        assert len(director) == 3

    def test_create(self):
        data = {'id': '', 'name': ''}
        director = self.director_service.create(data)
        assert director is not None
        assert director.id == 3
        assert director.name == 'Сидоров'

    def test_delete(self):
        director = self.director_service.delete(1)
        assert director is None

    def test_update(self):
        data = {'id': '', 'name': ''}
        director = self.director_service.update(data)
        assert director.id == 4
        assert director.name == 'Тютелькин'
