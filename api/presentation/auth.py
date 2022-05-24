from flask import request
from utils.presentation.api_resource import Resource

from api.domain.auth import Auth as AuthLogic

def ignore_func(*args, **kwargs):
    pass

class Auth(Resource):

    def post(self, action):
        data = request.json or {}
        function = {
            "logout": AuthLogic.logout,
            "login": AuthLogic.login,
            "register": AuthLogic.register,
            "authorization": AuthLogic.authorization
        }.get(action, ignore_func)
        # try:
        result = function(**data)
        # except Exception:
            # return "", 500
        if not result:
            return "", 503
        return result