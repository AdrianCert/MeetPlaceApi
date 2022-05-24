from utils.domain.models import Model


class EventSlot(Model):
    id: str
    timestamp_start: float
    timestamp_end: float
    hall_id: str
    duration: int
    status: str
    reservable: bool
    title: str
    details: str

    class Meta:
        fields = [
            "id",
            "timestamp_start",
            "timestamp_end",
            "hall_id",
            "duration",
            "status",
            "reservable",
            "title",
            "details"
        ]