from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_one(self, uid):
        return self.session.query(Genre).get(uid)

    def create(self, genre_id):
        ent = Genre(**genre_id)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, genre_id):
        genre = self.get_one(genre_id.get("id"))

        genre.name = genre_id.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, uid):
        genre = self.get_one(uid)

        self.session.delete(genre)
        self.session.commit()
