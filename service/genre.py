from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all_genres()

    def create(self, genre_id):
        return self.dao.create(genre_id)

    def delete(self, genre_id):
        self.dao.delete(genre_id)

    def update(self, genre_id):
        self.dao.update(genre_id)
        return self.dao