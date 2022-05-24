from utils.domain.models import Model


class Tag(Model):
    id: str
    name: str

    class Meta:
        fields = [
            "id",
            "name"
        ]