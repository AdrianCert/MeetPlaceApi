from utils.domain.repository import RepositoryFactory
from utils.permision import ResurcePermission
from utils.presentation.api_resource import RestResurce
from api.domain.entities.provider import Provider as ProviderModel
from common import PROVIDER_TABLE


class Provider(RestResurce):
    repository = RepositoryFactory(ProviderModel, PROVIDER_TABLE)
    model = ProviderModel
    permision = ResurcePermission()