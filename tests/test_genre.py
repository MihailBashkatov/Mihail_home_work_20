import pytest
from service.genre import GenreService


class TestgenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(5)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == 'Кино'

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert genre is not None
        assert type(genre) == list
        assert len(genre) == 3

    def test_create(self):
        data = {'id': '', 'name': ''}
        genre = self.genre_service.create(data)
        assert genre is not None
        assert genre.id == 3
        assert genre.name == 'Мульт'

    def test_delete(self):
        genre = self.genre_service.delete(1)
        assert genre is None

    def test_update(self):
        data = {'id': '', 'name': ''}
        genre = self.genre_service.update(data)
        assert genre.id == 4
        assert genre.name == 'Док'
