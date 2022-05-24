from utils.domain.repository import RepositoryFactory
from utils.permision import ResurcePermission
from utils.presentation.api_resource import RestResurce
from api.domain.entities.event_slot import EventSlot as EventSlotModel
from common import EVENT_SLOT_TABLE

class EventSlot(RestResurce):
    repository = RepositoryFactory(EventSlotModel, EVENT_SLOT_TABLE)
    model = EventSlotModel
    permision = ResurcePermission()
