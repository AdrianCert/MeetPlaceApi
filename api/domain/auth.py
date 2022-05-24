import os
import hashlib
import hmac

from uuid import uuid4
from typing import Tuple
from utils.data.datasource.mongo_db import MongoManager
from utils.domain.repository import RepositoryFactory
from utils.domain.exception import ModelNotFoundException
from api.domain.entities.user import User
from common import (
    MONGO_DB_CONFIG,
    USERS_TABLE,
    TOKENS_TABLE
)


def hash_new_password(password: str) -> Tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(32)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash

def is_correct_password(salt: bytes, pw_hash: bytes, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )


class Auth:
    mongo_manager = MongoManager(**MONGO_DB_CONFIG)

    @classmethod
    def _getuser(cls, user):
        with cls.mongo_manager:
            user_data = cls.mongo_manager.conn[USERS_TABLE].find_one({
                "$or": [
                    { "username": user },
                    { "email": user }
                ]
            })
            if not user_data:
                return None
            return user_data

    @classmethod
    def login(cls, user, password):
        user_data: dict = cls._getuser(user)
        if not user_data:
            return {
                "status": 404,
                "reason": "User not found!"
            }
        pw_data = user_data.get('password')
        salt, pw_hash = pw_data[:32], pw_data[32:]
        if not is_correct_password(salt, pw_hash, password):
            return {
                "status": 403,
                "reason": "Password not good!"
            }
        token_data = {
            'token': f"{uuid4()}",
            'user_id': f"{user_data['_id']}"
        }
        result = cls.mongo_manager.conn[TOKENS_TABLE].insert_one(token_data)
        if result.inserted_id:
            token_data['id'] = result.inserted_id
            return result
        return {
            "status": 402,
            "reason": "Could not generate token!"
        }

    @classmethod
    def register(cls, user, password):
        user_data = cls._getuser(user)
        salt, pw_hash = hash_new_password(password)
        with cls.mongo_manager as mng:
            result = mng.conn[USERS_TABLE].update_one({'_id': user_data['_id']}, {
                "$set": {
                    "password": salt + pw_hash
                }
            })
            if not result.modified_count == 1:
                return None
            return User.from_json(user_data).as_dict()

    @classmethod
    def logout(cls, token):
        with cls.mongo_manager as mng:
            result = mng.conn[TOKENS_TABLE].delete_one({'token': token})
        return result.deleted_count == 1

    @classmethod
    def authorization(cls, token):
        with cls.mongo_manager as mng:
            result = mng.conn[TOKENS_TABLE].find_one({'token': token})
            if not result:
                return None
            return User.from_json(result).as_dict()