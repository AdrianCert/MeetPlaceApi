from utils.domain.models import Model


class EventHall(Model):
    id: str
    name: str
    photoUrls: list[str]
    tags: list[str]
    slots: list[str]
    details: str
    provider: str

    class Meta:
        fields = [
            "id",
            "name",
            "photoUrls",
            "tags",
            "slots",
            "details",
            "provider"
        ]