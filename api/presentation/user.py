from utils.domain.repository import RepositoryFactory
from utils.permision import ResurcePermission
from utils.presentation.api_resource import RestResurce
from api.domain.entities.user import User as UserModel


class User(RestResurce):
    repository = RepositoryFactory(UserModel, "users")
    model = UserModel
    permision = ResurcePermission()
