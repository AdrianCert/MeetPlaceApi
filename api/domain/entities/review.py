from utils.domain.models import Model


class Review(Model):
    id: str
    grade: int
    user_id: int
    user: dict
    event_id: int
    event: dict
    name: str

    class Meta:
        fields = [
            "id",
            "grade",
            "user_id",
            "user",
            "event_id",
            "event",
            "name"
        ]