from utils.domain.repository import RepositoryFactory
from utils.permision import ResurcePermission
from utils.presentation.api_resource import RestResurce
from api.domain.entities.category import Category as CategoryModel
from common import CATAGORY_TABLE


class Category(RestResurce):
    repository = RepositoryFactory(CategoryModel, CATAGORY_TABLE)
    model = CategoryModel
    permision = ResurcePermission()
