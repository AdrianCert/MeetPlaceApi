from utils.domain.entites import BaseEntity
from utils.reflection import class_annotations


class Model:

    class Meta:
        fields: list[str]

    def as_dict(self):
        data = {}
        for field in self.Meta.fields:
            if hasattr(self, field):
                data[field] = getattr(self, field)
        return data

    def to_entity(self) -> BaseEntity:
        raise NotImplementedError

    def post_init(self, exbin: dict):
        mongo_id = exbin.get('_id')
        if mongo_id:
            self.id = f"{mongo_id}"
        pass

    @classmethod
    def from_json(cls, data: dict) -> 'Model':
        instance = cls()
        anotations = class_annotations(cls)
        exbin = {}
        for attr, val in data.items():
            attr_type = anotations.get(attr)
            if not attr_type:
                exbin[attr] = val
                continue
            # if nest Model class then convert from dict
            if not isinstance(val, attr_type):
                raise AttributeError(f"{attr} should be an instance of {attr_type}")
            setattr(instance, attr, val)

        instance.post_init(exbin)
        return instance