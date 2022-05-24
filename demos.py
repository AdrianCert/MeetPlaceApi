from flask import Flask
from flask import request
from flask_restful import Resource, Api
from pymongo import MongoClient
import logging

app = Flask(__name__)
api = Api(app)

mongo_uri = 'mongodb://fiicloud:bEuJJUJdEYAGt2T4UgFnfrnMLdrNH9QRVhGLhb2YSgHUW8QqMTAtEDXJzJn1E0cktrwnV6aCmXNhzmgTyIfptg==@fiicloud.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@fiicloud@'

data = [{
    "id" : 0,
    "nrOfSeats" : "4 passengers",
    "speed" : "100 km/h in 4 seconds",
    "gearbox" : "Automatic gearbox",
    "type" : "Electric",
    "imgSrc" : "https://images.unsplash.com/photo-1453491945771-a1e904948959?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
    "carName" : "Tesla Model S",
    "price" : "168.00"
}]

def get_item(id = None):
    if id is None:
        return None, -1
    for index, item in enumerate(data):
        if item['id'] == id:
            return item, index
    return None, -1

class DataSource:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name

    def __enter__(self):
        print(self.db_name)
        self.client = MongoClient(self.uri)
        self.conn = self.client[self.db_name]
        print(self.client)
        print(self.conn)
        return self

    def __exit__(self, type, value, traceback):
        pass

datasource_conf = {
    "uri": mongo_uri,
    "db_name": "ccdb"
}

from api.presentation.user import User as UserApi

api.add_resource(UserApi, '/users', '/users/', '/users/<id>')


def car_projection(document: dict) -> dict:
    return {k:v for k,v in document.items() if k not in ['_id']}

@api.resource('/cars/<id>')
class Car(Resource):
    def get(self, id):
        print(id)
        if id:
            return get_item(int(id))[0]
        return [i for i in data]

    def put(self, id):
        print(request.json)
        item, index = get_item(id)
        item.update(request.json)
        data[index] = index

    def delete(self):
        pass


@api.resource('/cars')
class Cars(Resource):
    def get(self):
        with DataSource(**datasource_conf) as dsc:
            return [car_projection(item) for item in dsc.conn['cars'].find({})]

    def post(self):
        data = request.json
        if isinstance(data, dict):
            data = [data]
        with DataSource(**datasource_conf) as dsc:
            operation_result = dsc.conn['cars'].insert_many(data)
            return [f"{_id}" for _id in operation_result.inserted_ids]


_default = type("DefaultType")

class MongoComponent(Resource):
    _datasource = DataSource(**datasource_conf)
    table = _default
    modelclass = _default

    def _get_item(self, id):
        with self._datasource:
            nfo = self._datasource.conn[self.table].find({"_id": id})
            return self.modelclass(**nfo)

    def _get_collection(self):
        with self._datasource:
            nfo = self._datasource.conn[self.table].find()
            return list(map(self.modelclass.entity, ))
        pass

    def get(self, id = _default):
        if id == _default:
            return self._get_collection()
        return self._get_item(id)
        #     with DataSource(**datasource_conf) as dsc:
        #     return [car_projection(item) for item in dsc.conn['cars'].find({})]

        #     return get_item(int(id))[0]
        # return [i for i in data]

    def put(self, id):
        print(request.json)
        item, index = get_item(id)
        item.update(request.json)
        data[index] = index

    def delete(self):
        pass

    # def get(self):
    #     with DataSource(**datasource_conf) as dsc:
    #         return [car_projection(item) for item in dsc.conn['cars'].find({})]

    def post(self):
        data = request.json
        if isinstance(data, dict):
            data = [data]
        with self._datasource:
            operation_result = self._datasource.conn['cars'].insert_many(data)
            return [f"{_id}" for _id in operation_result.inserted_ids]

from dataclasses import (
    dataclass,
    is_dataclass,
    asdict,
    field
)

@dataclass
class User:
    id: str
    name: str
    email: str
    _id: str
    
    def entity(self):
        pass

@api.resource('/users', '/users/', '/users/<id>')
class RestUser(MongoComponent):
    table = "Users"
    modelclass = User


if __name__ == '__main__':
    app.run(debug=True)