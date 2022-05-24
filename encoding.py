import json
from functools import partial
from dataclasses import (
    dataclass,
    is_dataclass,
    asdict,
    field
)

class EnhancedJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if is_dataclass(o):
                return asdict(o)
            return super().default(o)

json.dumps = partial(json.dumps, cls=EnhancedJSONEncoder)


@dataclass
class User:
    id: str
    name: str
    email: str

input = {
    "id": "12345",
    "name": "Adrian",
    "email": "Adrian",
    "extra": "123"
}

x = User(**input)
# x = User(id="12345", name="Adrian", email="a@rian.com")
print(json.dumps(x, indent=2))
# json.dumps(foo, cls=EnhancedJSONEncoder)
