from utils.domain.models import Model


class User(Model):
    id: str
    username: str
    firstName: str
    lastName: str
    email: str
    phone: str
    userStatus: str

    class Meta:
        fields = [
            "id",
            "username",
            "firstName",
            "lastName",
            "email",
            "phone",
            "userStatus"
        ]