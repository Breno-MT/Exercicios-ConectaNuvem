from requests import request
from tinydb import TinyDB, Query

Find = Query()

db = TinyDB('src/app/db/db.json')
