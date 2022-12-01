from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all_directors()

    def create(self, director_id):
        return self.dao.create(director_id)

    def delete(self, director_id):
        self.dao.delete(director_id)

    def update(self, director_id):
        self.dao.update(director_id)
        return self.dao