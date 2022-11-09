import os

class Config(object):
    MASTER_KEY = os.getenv('master_key')
    MONGO_URI = os.getenv('mongo_uri')
    