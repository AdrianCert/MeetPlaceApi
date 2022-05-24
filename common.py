from pathlib import Path

MONGO_DB_URI = 'mongodb://fiicloud:bEuJJUJdEYAGt2T4UgFnfrnMLdrNH9QRVhGLhb2YSgHUW8QqMTAtEDXJzJn1E0cktrwnV6aCmXNhzmgTyIfptg==@fiicloud.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@fiicloud@'
certificate = Path(__file__).parent.joinpath("ca-certificate.crt").absolute().__str__().replace('\\', "/")
print(certificate)
MONGO_DB_URI = f'mongodb://doadmin:Wm7h5267cr!ShAd@db-mongodb-fra1-51328-252692f1.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-fra1-51328&tlsCAFile={certificate}'

MONGO_DB_CONFIG = {
    "uri": MONGO_DB_URI,
    "db_name": "admin"
}

USERS_TABLE = 'users'
TOKENS_TABLE = 'tokens'
EVENT_SLOT_TABLE = 'event_slots'
CATAGORY_TABLE = 'categories'
EVENT_HALL_TABLE = 'event_halls'
PROVIDER_TABLE = 'providers'
REVIEW_TABLE = 'reviews'
TAG_TABLE = 'tags'