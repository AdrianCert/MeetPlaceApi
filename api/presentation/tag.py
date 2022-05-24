from utils.domain.repository import RepositoryFactory
from utils.permision import ResurcePermission
from utils.presentation.api_resource import RestResurce
from api.domain.entities.tag import Tag as TagModel
from common import TAG_TABLE


class Tag(RestResurce):
    repository = RepositoryFactory(TagModel, TAG_TABLE)
    model = TagModel
    permision = ResurcePermission()