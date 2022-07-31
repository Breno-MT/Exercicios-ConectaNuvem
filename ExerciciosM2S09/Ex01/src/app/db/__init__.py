from requests import request
from tinydb import TinyDB, Query

User = Query()

db = TinyDB('src/app/db/db.json')
