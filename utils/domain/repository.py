from utils.data.datasource.mongo_db import MongoManager
from bson.objectid import ObjectId
from utils.domain.models import Model
from common import MONGO_DB_CONFIG


class BaseRepository:
    def get(*args, **kwargs) -> Model:
        raise NotImplementedError

    def get_all(*args, **kwargs) -> list[Model]:
        raise NotImplementedError

    def delete(*args, **kwargs) -> bool:
        raise NotImplementedError

    def update(*args, **kwargs) -> Model:
        raise NotImplementedError

    def create(*args, **kwargs) -> Model:
        raise NotImplementedError


class MongoRepository(BaseRepository):
    modelcls: Model
    source: MongoManager
    table: str

    def __init__(self, model, source, table):
        self.modelcls = model
        self.source = source
        self.table = table

    def get(self, id, *args, **kwargs) -> Model:
        with self.source:
            if not isinstance(id, ObjectId):
                id = ObjectId(id)
            data = self.source.conn[self.table].find_one({'_id': id})
            if not data:
                return None
            return self.modelcls.from_json(data)

    def get_all(self, *args, **kwargs) -> list[Model]:
        with self.source:
            data = self.source.conn[self.table].find()
            data = list(map(self.modelcls.from_json, data))
            return data

    def delete(self, id, *args, **kwargs) -> bool:
        with self.source:
            nfo = self.source.conn[self.table].delete_one({'_id': id})
            return nfo.deleted_count == 1

    def update(self, id, data: 'Model' , *args, **kwargs) -> Model:
        with self.source:
            data = data.as_dict()
            if data.get('id'):
                data.pop('id')
            nfo = self.source.conn[self.table].update_one({'_id': id}, { "$set": data})
        return self.get(id)

    def create(self, data: 'Model', *args, **kwargs) -> Model:
        with self.source:
            data = data.as_dict()
            nfo = self.source.conn[self.table].insert_one(data)
        return self.get(nfo.inserted_id)


def RepositoryFactory(model, table) -> MongoRepository:
        return MongoRepository(**{
            "model": model,
            "source": MongoManager(**MONGO_DB_CONFIG),
            "table": table
        })