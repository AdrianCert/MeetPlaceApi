from utils.domain.repository import RepositoryFactory
from utils.permision import ResurcePermission
from utils.presentation.api_resource import RestResurce
from api.domain.entities.review import Review as ReviewModel
from common import REVIEW_TABLE


class Review(RestResurce):
    repository = RepositoryFactory(ReviewModel, REVIEW_TABLE)
    model = ReviewModel
    permision = ResurcePermission()