from utils.domain.repository import BaseRepository
from utils.domain.models import Model
from utils.permision import ResurcePermission

from flask import request
from flask_restful import Resource

# from utils.profile import performance

from functools import wraps

def authorization(actual_method):
    @wraps(actual_method)
    def wrapper(self, *args, **kwargs):
        # do your validation here
        print(self)
        print(request.headers.get('Authorization'))
        return actual_method(self, *args, **kwargs)

    return wrapper


class RestResurce(Resource):
    repository: BaseRepository
    model: Model
    permision: ResurcePermission

    @authorization
    def get(self, id = None):
        if id:
            nfo = self.repository.get(id=id)
            if nfo:
                return nfo.as_dict()
            return {}, 404

        nfo = self.repository.get_all()
        return list(map(self.model.as_dict, nfo))

    @authorization
    def put(self, id):
        model = self.model.from_json(request.json)
        nfo = self.repository.update(id=id, data=model)
        return nfo.as_dict()

    @authorization
    def delete(self, id):
        nfo = self.repository.delete(id=id)
        return nfo

    @authorization
    def post(self):
        model = self.model.from_json(request.json)
        nfo = self.repository.create(data=model)
        return nfo.as_dict()

