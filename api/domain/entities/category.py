from utils.domain.models import Model


class Category(Model):
    id: str
    name: str

    class Meta:
        fields = [
            "id",
            "name"
        ]