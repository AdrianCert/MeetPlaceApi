from utils.domain.models import Model


class Provider(Model):
    id: str
    halls: list[str]
    qualifying: list[str]
    reviews: list[str]
    owner: str

    class Meta:
        fields = [
            "id",
            "halls",
            "qualifying",
            "reviews",
            "owner"
        ]