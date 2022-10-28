import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(5)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == 'Кино'

    def test_get_all(self):
        movie = self.movie_service.get_all()
        assert movie is not None
        assert type(movie) == list
        assert len(movie) == 3

    def test_create(self):
        data = {'id': '', 'title': ''}
        movie = self.movie_service.create(data)
        assert movie is not None
        assert movie.id == 3
        assert movie.title == 'Мульт'

    def test_delete(self):
        movie = self.movie_service.delete(1)
        assert movie is None

    def test_update(self):
        data = {'id': '', 'title': ''}
        movie = self.movie_service.update(data)
        assert movie.id == 4
        assert movie.title == 'Док'
