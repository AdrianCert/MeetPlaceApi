from utils.reflection import class_annotations

class PermissionClassBase:
    title = "BasePermission"

class Everyone(PermissionClassBase):
    title = "Everyone"
    f_auth = False

class IsAuthentificated(PermissionClassBase):
    title = "Authentificated User"
    f_auth = True

class AdminUser(IsAuthentificated):
    title = "Admin User"
    f_admin = True

class SuperUser(AdminUser):
    title = "Super User"
    f_superuser = True

class RegularUser(IsAuthentificated):
    title = "Regular User"

class ResurcePermission:
    get: str = [IsAuthentificated]
    post: str = [IsAuthentificated]
    put: str = [IsAuthentificated]
    delete: str = [IsAuthentificated]

    def __init__(self, **kwargs):
        annotations = class_annotations(self.__class__)
        for attr, value in kwargs.items():
            if attr in annotations:
                setattr(self, attr, value)