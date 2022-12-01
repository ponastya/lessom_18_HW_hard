from dao.movie import MovieDAO

class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all_movies()
        return movies

    def create(self, movie_id):
        return self.dao.create(movie_id)

    def delete(self, movie_id):
        self.dao.delete(movie_id)

    def update(self, movie_id):
        self.dao.update(movie_id)
        return self.dao