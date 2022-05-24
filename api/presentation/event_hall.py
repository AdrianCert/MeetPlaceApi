from utils.domain.repository import RepositoryFactory
from utils.permision import ResurcePermission
from utils.presentation.api_resource import RestResurce
from api.domain.entities.event_hall import EventHall as EventHallModel
from common import EVENT_HALL_TABLE


class EventHall(RestResurce):
    repository = RepositoryFactory(EventHallModel, EVENT_HALL_TABLE)
    model = EventHallModel
    permision = ResurcePermission()
