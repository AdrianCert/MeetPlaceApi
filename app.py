from flask import Flask
from flask_restful import Api
from api.presentation.auth import Auth as AuthApi
from api.presentation.category import Category as CategoryApi
from api.presentation.event_slot import EventSlot as EventSlotApi
from api.presentation.event_hall import EventHall as EventHallApi
from api.presentation.provider import Provider as ProviderApi
from api.presentation.review import Review as ReviewApi
from api.presentation.tag import Tag as TagApi
from api.presentation.user import User as UserApi

app = Flask(__name__)
api = Api(app)

api.add_resource(AuthApi, '/auth/<action>')
api.add_resource(CategoryApi, '/category', '/category/', '/category/<id>')
api.add_resource(EventSlotApi, '/event_slot', '/event_slot/', '/event_slot/<id>')
api.add_resource(EventHallApi, '/event_hall', '/event_hall/', '/event_hall/<id>')
api.add_resource(ProviderApi, '/provider', '/provider/', '/provider/<id>')
api.add_resource(ReviewApi, '/review', '/review/', '/review/<id>')
api.add_resource(TagApi, '/tag', '/tag/', '/tag/<id>')
api.add_resource(UserApi, '/users', '/users/', '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)
